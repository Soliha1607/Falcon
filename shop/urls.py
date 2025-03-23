from django.urls import path

from shop import views

from shop.views import (
IndexView, ProductDetail,
    CustomerListView, CustomerDetailView,
    CustomerCreateView, CustomerUpdateView, CustomerDeleteView
)

urlpatterns = [
    path('', views.index, name='index'),
    path('products_list/<slug:category_slug>', IndexView.as_view(), name='products_list_by_category'),
    path('products/<int:product_id>/', ProductDetail.as_view(), name='product_detail'),
    path('customers/', CustomerListView.as_view(), name='customers'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('customers/new/', CustomerCreateView.as_view(), name='customer_add'),
    path('customers/<int:pk>/edit/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customers/<int:customer_id>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),
]