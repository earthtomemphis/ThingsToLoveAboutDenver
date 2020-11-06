from django.urls import path
from . views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategorylistView, LikeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('new-post/', AddPostView.as_view(), name='new-post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>', CategoryView, name='category'),
    path('category-list/', CategorylistView, name='category-list'),
    path('like/<int:pk>', LikeView, name='like_post'),
]