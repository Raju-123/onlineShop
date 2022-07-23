from django.urls import path
from . import views

urlpatterns = [
    path('list', views.list),
    path('create', views.create),
]