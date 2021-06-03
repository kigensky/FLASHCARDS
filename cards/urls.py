from django.urls import path
from . import views
# from .views import FlashCardsDetailView



urlpatterns = [
    path('', views.home, name='cards-home'),
    # path('FlashCards/<int:pk>/', FlashCardsDetailView.as_view(), name='cards-detail'),
    path('cards/new', views.flashCardsCreateView, name='cards-create'),
    
]    