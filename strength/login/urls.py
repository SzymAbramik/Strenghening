from django.urls import path
from . import views


app_name = 'login'

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/<slug:slug>/', views.profilePage, name='profile'),

] 
