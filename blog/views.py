from django.views.generic import ListView, DetailView

from blog.models import PostModel


class PostsListView(ListView):
    queryset = PostModel.objects.order_by('-pk')
    template_name = 'blog-video-format.html'


class PostDetailView(DetailView):
    template_name = 'blog-details-right-sidebar.html'
    model = PostModel
