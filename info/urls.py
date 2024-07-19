from django.urls import path

from info.views import BlogListView, BlogDetailDetailView, CommentCreateView

app_name = 'info'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('<int:pk>/', BlogDetailDetailView.as_view(), name='blog-detail'),
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment'),
]
