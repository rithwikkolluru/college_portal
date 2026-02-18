from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('faculty/', views.faculty_page, name='faculty'),
    path('courses/', views.courses_page, name='courses'),
    path('placements/', views.placements_page, name='placements'),
    path('contact/', views.contact_page, name='contact'),
    path('register/', views.register, name='register'),
]
