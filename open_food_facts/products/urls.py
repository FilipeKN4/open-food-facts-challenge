from django.urls import path
from products import views

urlpatterns = [
    path('overview/', views.ProductsOverview.as_view(), name='products_overview'),
    path('products/', views.ProductsList.as_view(), name='products_list'),
    path('products/<str:code>/', views.ProductDetail.as_view(), name='product_detail')
]
