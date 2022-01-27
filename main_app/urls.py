from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.products_index, name='index'),
    path('products/<int:product_id>/', views.products_detail, name='detail'),
    path('cart/', views.cart_index, name='cart_index'),
    path('cart/<int:cart_id>/', views.cart_detail, name='cart_detail'),
    path('cart/<int:pk>/update/', views.SubCartUpdate.as_view(), 
    name='add_quantity'),
    path('cart/<int:pk>/delete/', views.SubCartDelete.as_view(), 
    name='cart_delete'),
    path('cart/create/', views.SubCartCreate.as_view(), name='cart_create'),
    path('product/<int:product_id>/create/', views.add_to_cart, name="add_to_cart"),
    path('accounts/signup/', views.signup, name='signup'),
    # path('user/create/', views.CartCreate.as_view(), name='user_create'),
]