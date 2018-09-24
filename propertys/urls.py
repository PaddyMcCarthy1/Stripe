from django.urls import path
from . import views


urlpatterns = [
    path('property/', views.PropertyListView.as_view(), name='property_list'),
    path('property/<int:pk>/', views.PropertyDetailView.as_view(), name='property_detail'),
    path('property/<int:pk>/edit/', views.PropertyUpdateView.as_view(), name='property_update'),
    path('property/<int:pk>/delete/', views.PropertyDeleteView.as_view(), name='property_delete'),
    path('property/create/', views.PropertyCreateView.as_view(), name='property_create'),
]

