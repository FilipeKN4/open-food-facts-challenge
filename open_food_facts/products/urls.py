from django.urls import path
from products import views

urlpatterns = [
    path('overview/', views.products_overview, name='products_overview'),
    path('products/', views.products_list, name='products_list'),
    path('products/<str:code>/', views.product_detail, name='product_detail')
]
