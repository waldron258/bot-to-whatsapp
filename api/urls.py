from django.urls import path
from . import views

urlpatterns = [
    path('', views.getInformation, name='api-overview'),
#    path('customer-list/', views.customerList, name='customer-list'),
#    path('customer-detail/<str:pk>/', views.customerDetail, name='customer-detail'),
    path('customer-create/', views.customerCreate, name='customer-create'),
]
