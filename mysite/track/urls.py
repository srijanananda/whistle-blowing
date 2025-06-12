from django.urls import path
from . import views

urlpatterns = [
    path('', views.track_home, name='track_home'),
]
