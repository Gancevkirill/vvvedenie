from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.index, name='home',kwargs = {'name':'Зиятдинова Лилия Руслановна','age':'16','interes':'есть'}),
    path('about',views.about,name = 'about',kwargs = {'city':'Казань','eval':'хорошая'}),
    path('contacts', views.contacts, name='contacts'),

]
