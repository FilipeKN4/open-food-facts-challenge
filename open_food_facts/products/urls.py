# Django imports
from django.urls import path

# Products app imports
from products import views

urlpatterns = [
    # API Details endpoint
    path('', views.APIDetails.as_view(), name='api_details'),
    
    # Products app overview endpoint
    path('overview/', views.ProductsOverview.as_view(), name='products_overview'),
    
    # Products endpoints
    path('products/', views.ProductsList.as_view(), name='products_list'),
    path('products/<str:code>/', views.ProductDetail.as_view(), name='product_detail'),
    
    # Products update history endpoints
    path('products_update_history/', views.ProductsUpdateHistoryList.as_view(), name='products_update_history_list'),
    path('products_update_history/<int:pk>/', views.ProductsUpdateHistoryDetail.as_view(), name='products_update_history_detail')
]
