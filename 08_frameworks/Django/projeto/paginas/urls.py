from django.urls import path
from . import views

app_name = 'paginas'

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
]