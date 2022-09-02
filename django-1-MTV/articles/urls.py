
from django.urls import path
from . import views
app_name = 'articles'
urlpatterns = [
    path('index/', views.index),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/<name>/', views.hello),
]
