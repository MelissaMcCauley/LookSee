from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # previous login view that was constructed manually:
    # path('login/', views.user_login, name='login'),
    # Django class-based authentication views:
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logged_out.html'), name='logout'),
    path('', views.dashboard, name='dashboard'),

]