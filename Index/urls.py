from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index_c.html', views.index_c, name='index_c'),
    path('index_output.html', views.index_output, name='index_output'),
    path('dic_output.html', views.dic_output, name='dic_output')
]
