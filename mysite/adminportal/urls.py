from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_login, name='admin_login'),
    path('dashboard/', views.dashboard, name='admin_dashboard'),
    path('logout/', views.admin_logout, name='admin_logout'),
    path('update_status/<int:complaint_id>/', views.update_status, name='update_status'),
    path('delete/<int:complaint_id>/', views.delete_complaint, name='delete_complaint'),
]
