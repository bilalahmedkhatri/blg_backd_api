from django.urls import path
from .views import (
    PostList, PostDetail, PostCreate, PostUpdate, PostDelete, UserList, UserDetail,
    CategoryList, CategoryDetail, TagList, TagDetail, CreateCategory, DeleteCategory, UserRegistrationView,
    LoginView, LogoutView
)

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<slug:slug>/', PostDetail.as_view(), name='post-detail'),
    
    # user registration
    path('auth/register/', UserRegistrationView.as_view(), name='user-register'),
    
    ### dashboard accessable urls
    path('dashboard/users/', UserList.as_view(), name='user-list'),
    path('dashboard/users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('dashboard/category/create/', CreateCategory.as_view(), name='category-create'),
    path('dashboard/category/<int:pk>/delete/', DeleteCategory.as_view(), name='category-delete'),
    path('dashboard/category/', CategoryList.as_view(), name='category-list'),
    path('dashboard/category/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('dashboard/tags/', TagList.as_view(), name='tag-list'),
    path('dashboard/tags/<int:pk>/', TagDetail.as_view(), name='tag-detail'),
    path('dashboard/posts-create/', PostCreate.as_view(), name='post-create'),
    path('dashboard/posts/<slug:slug>/update/', PostUpdate.as_view(), name='post-update'),
    path('dashboard/posts/<slug:slug>/delete/', PostDelete.as_view(), name='post-delete'),
    
    path('dashboard/auth/login/', LoginView.as_view(), name='login'),
    path('dashboard/auth/logout/', LogoutView.as_view(), name='logout'),
]