from django.http import HttpResponse
from django.shortcuts import render
import speech_recognition as sr

def index(request):
    """
    Заглавная страница портала
    """
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

def speech_text_speech(request):
    """
    Голос в текст и обратно в голос
    """
    template_name = 'portal/modules.html'
    context = {
        'title': 'Голос в текст и обратно'
    }
    return render(request, template_name=template_name, context=context)