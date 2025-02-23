from django.urls import path
from . import views  # Import the entire views module
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='posts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='homepage'), name='logout'),
    path('', views.homepage, name='homepage'),

    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('profile/', views.profile, name='profile'),

]
