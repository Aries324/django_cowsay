from django.urls import path
from cowsay_project import views


urlpatterns = [
    path('', views.index),
    path('history', views.history)
]