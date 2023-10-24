from django.urls import path
from .views import BlogHome, BlogPostCreate, BlogDetailView, BlogUpdateView, BlogDeleteView


urlpatterns = [
    path('', BlogHome.as_view(), name="blogHome"),
    path('blog-create/', BlogPostCreate.as_view(), name = 'blog-create'),
    path('<int:pk>/', BlogDetailView.as_view(), name = 'detail'),
    path('<int:pk>/update', BlogUpdateView.as_view(), name = 'blogUpdate'),
    path('<int:pk>/delete', BlogDeleteView.as_view(), name = 'blogDelete'),
]