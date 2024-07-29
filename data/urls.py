from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.user_logout, name='logout'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('profile/<str:username>/', views.User_Profile, name='profile'),
    path('edit/profile/', views.User_Profile_Edit, name='edit'),
    path('follow/<str:username>/', views.follow, name='follow'),
    path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
    path('post/create/', views.create_post, name='create'),
    path('page/post/<int:post_title>', views.post_page, name='post_page'),
    path('post/like/<int:post_title>', views.like_post, name='like'),
    path('post/unlike/<int:post_title>', views.unlike_post, name='unlike'),
    path('post/<int:post_id>/delete', views.delete_post, name='delete'),
    path('edit/<int:edit_post_id>/', views.edit_post, name='edit'),
    path('explore/', views.Explore, name='explore'),
    path('search/', views.search, name='search'),
]
