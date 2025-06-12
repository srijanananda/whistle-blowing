from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_complaint),  # 👈 This line handles /complaint/
    path('submit/', views.submit_complaint, name='submit_complaint'),
    path('track/', views.track_complaint, name='track_complaint'),
]
