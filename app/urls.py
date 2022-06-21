from django.urls import path
from . import views
from .views import SearchResultsView

urlpatterns = [
    path('', views.home, name='home'),
    
    path('register/', views.register, name='register'),
]