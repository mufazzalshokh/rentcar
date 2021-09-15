from django.urls import path

from blog.views import PostsListView, PostDetailView, CommentCreateView

app_name = 'posts'

urlpatterns = [
    path('', PostsListView.as_view(), name='list'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment'),
]
