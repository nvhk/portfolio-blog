from django.urls import path
from . import views

urlpatterns = [

    path('', views.blogi, name='blogi'),


]
