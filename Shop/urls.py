from django.urls import path
from .views import HomeView, ProductListView, ProductDetailView, ReviewCreateView, CartView, OrderListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('catalog/', ProductListView.as_view(), name='catalog'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/add_review/', ReviewCreateView.as_view(), name='add_review'),
    path('cart/', CartView.as_view(), name='cart'),
    path('orders/', OrderListView.as_view(), name='orders'),
]
