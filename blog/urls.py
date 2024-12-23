from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView


app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('<int:pk>/edit/', BlogUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='delete'),
]
