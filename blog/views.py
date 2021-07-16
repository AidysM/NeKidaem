from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from .models import Post
from .forms import PostForm


class PostListView(ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-created')
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class PostDetailView(DetailView):
    template_name = 'blog/post.html'
    queryset = Post.objects.all()

    def get_success_url(self):
        return self.request.path


class PostCreateView(CreateView):
    template_name = 'blog/post_create.html'
    form_class = PostForm
    success_url = '/blog/'


class PostUpdateView(UpdateView):
    template_name = 'blog/post_create.html'
    form_class = PostForm
    success_url = '/blog/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):
    template_name = 'blog/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/blog/'

