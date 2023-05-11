from django.urls import path
from . import views

app_name = 'diet'

urlpatterns = [
    path('', views.indexView, name='index'),
    path('<int:diet_id>/', views.detailView, name='detail'),
    path('submit_review/<int:diet_id>/', views.submit_review, name='submit_review'),
]
