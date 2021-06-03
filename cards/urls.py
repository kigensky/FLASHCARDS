from django.urls import path
from . import views
# from .views import FlashCardsDetailView



urlpatterns = [
    path('', views.home, name='cards-home'),
    # path('FlashCards/<int:pk>/', FlashCardsDetailView.as_view(), name='cards-detail'),
    path('cards/new', views.flashCardsCreateView, name='cards-create'),
    path('cards/delete/<int:id>/', views.flashCardsDelete, name='cards-delete'),
    path('cards/update/<int:id>/', views.flashCardsUpdate, name='cards-update'),
]    