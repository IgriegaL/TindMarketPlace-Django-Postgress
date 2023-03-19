from django.urls import path
from . import views
from .views import ProductListView


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add_product/', views.add_product, name='add_product'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('edit_product/<int:pk>/', views.edit_product, name='edit_product'),
    path('users/', views.user_list, name='user_list'),
    path('products/', ProductListView.as_view(), name='product_list'),

]