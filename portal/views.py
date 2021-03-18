from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    """
    Заглавная страница портала
    """
    template_name = 'portal/index.html'
    context = {
        'test': 'test'
    }
    return render(request, template_name=template_name, context=context)
