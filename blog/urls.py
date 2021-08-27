from django.urls import path

from blog.views import PostsListView, PostDetailView

app_name = 'posts'

urlpatterns = [
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('', PostsListView.as_view(), name='list'),
]
