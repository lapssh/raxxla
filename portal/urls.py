from django.urls import path

from portal.views import index

urlpatterns = [
    path('', index, name='index'),
]
