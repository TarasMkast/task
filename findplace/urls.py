
from django.urls import path
from . import views

urlpatterns = [
    path('main', views.main, name = 'main'),
    path('next', views.next_page, name = 'next')
]
