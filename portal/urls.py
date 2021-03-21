from django.urls import path

from portal.views import index, speech_text_speech, modules, show_lojso_page, show_organizmus_page

urlpatterns = [
    path('', index, name='index'),
    path('modules', modules, name='modules'),
    path('lojso', show_lojso_page, name='show_lojso_page'),
    path('organizmus', show_organizmus_page, name='show_organizmus_page'),
    path('speech_text_speech', speech_text_speech, name='speech_text_speech'),
]
