from django.urls import path
from .views import MainView

app_name = 'bmicalc'

urlpatterns = [
    path('', MainView, name='index'),
]
