from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from blog.forms import CommentModelForm
from blog.models import PostModel, PostTagModel


class PostsListView(ListView):
    template_name = 'blog-left-sidebar.html'

    def get_queryset(self):
        qs = PostModel.objects.order_by('-pk')
        tag = self.request.GET.get('tag')
        sort = self.request.GET.get('sort')

        if tag:
            qs = qs.filter(tags__id=tag)

        if sort:
            if sort == 'price':
                qs = sorted(qs, key=lambda i: i.get_price())
            elif sort == '-price':
                qs = sorted(qs, key=lambda i: i.get_price(), reverse=True)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = PostTagModel.objects.all()

        return context


class PostDetailView(DetailView):
    template_name = 'blog-video-format.html'
    model = PostModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = PostModel.objects.order_by('-pk')[:4]

        return context


class CommentCreateView(CreateView):
    form_class = CommentModelForm

    def form_valid(self, form):
        form.instance.post = get_object_or_404(PostModel, pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('posts:detail', kwargs={'pk': self.kwargs.get('pk')})
