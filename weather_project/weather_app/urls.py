from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('another-page/', views.another_page, name='another_page'),
]
