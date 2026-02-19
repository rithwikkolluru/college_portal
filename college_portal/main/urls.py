from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.base, name='base'),
    path('faculty/', views.faculty_page, name='faculty'),
    path('courses/', views.courses_page, name='courses'),
    path('placements/', views.placements_page, name='placements'),
    path('contact/', views.contact_page, name='contact'),

    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('register/', views.register_student, name='register'),
]
