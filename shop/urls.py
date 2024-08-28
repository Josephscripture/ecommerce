from django.urls import path
from . import views


urlpatterns=[
    path('', views.home ,name='home'),
    path('login_view', views.login_view ,name='login'),
    path('logout_view', views.logout_view ,name='logout'),
    path('signup_view', views.signup_view,name='signup'),
    path('update_view', views.update_view,name='update'),
    path('update_category', views.update_category, name='category'),
    path('delete_view/<str:pk>/', views.delete_view, name='delete'),
    # path('cart/<str:pk>/', views.cart, name='add-to-cart'),
    
]