import sys

from django.shortcuts import render
from lib.speech_text_speech import record_volume
from loguru import logger
import speech_recognition as sr

@logger.catch()
def index(request):
    """
    Заглавная страница портала
    """
    logger.debug('Пользователь зашёл на главную.')
    template_name = 'portal/index.html'
    context = {
        'test': 'test',
        'title': 'Главная страница'
    }
    return render(request, template_name=template_name, context=context)

def modules(request):
    """
    страница списка модулей
    """
    modules = ['speech-text-speech']
    template_name = 'portal/modules.html'
    context = {
        'title': 'Список модулей',
        'modules': modules,
    }
    return render(request, template_name=template_name, context=context)


def show_lojso_page(request):
    template_name = 'portal/lojso.html'
    context = {
        'title': 'Страница Lojso',
        'text': 'text',
    }
    return render(request, template_name=template_name, context=context)


def show_organizmus_page(request):
    template_name = 'portal/organizmus.html'
    context = {
        'title': 'Страница Organizmus',
        'text': 'text',
    }
    return render(request, template_name=template_name, context=context)


def speech_text_speech(request):
    """
    Голос в текст и обратно в голос
    """
    text = record_volume()

    template_name = 'portal/speech-text-speech.html'
    context = {
        'title': 'Голос в текст и обратно',
        'text': text,

    }
    return render(request, template_name=template_name, context=context)


logger.add('debug.log', format='{time} {level} {message}', level='DEBUG', rotation='10 KB', compression='zip' )
