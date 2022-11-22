from django.urls import path
from . import views

urlpatterns = [path('b/', views.b, name='b'),
               path('', views.frontpage, name='frontpage'),
               path('b/thread/<int:id>', views.thread, name='thread')]
