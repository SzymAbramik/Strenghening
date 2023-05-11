from django.urls import path
from . import views

app_name = 'training'

urlpatterns = [
    path('', views.indexView, name='index'),
    path('<int:training_id>/', views.detailView, name='detail'),
    path('submit_review/<int:training_id>/', views.submit_review, name='submit_review'),
]
