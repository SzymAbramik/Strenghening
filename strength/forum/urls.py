from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.indexView, name='index'),
    path('add/', views.CreatePost.as_view(), name='add'),
    path('like/', views.like_comment, name='like'),
    path('<slug:slug>/delete/', views.DeletePost.as_view(), name='delete'),
    path('<slug:slug>/', views.DetailView.as_view(), name='detail'),
]
