from django.urls import path

from portal.views import index, speech_text_speech, modules

urlpatterns = [
    path('', index, name='index'),
    path('modules', modules, name='modules'),
    path('speech_text_speech', speech_text_speech, name='speech_text_speech'),
]
