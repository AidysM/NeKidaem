from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.views.generic.edit import FormView

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
        # context['filter'] = AdvertFilter(self.request.GET,
        #                                  queryset=self.get_queryset())  # вписываем фильтр
        return context


class PostDetailView(DetailView):
    template_name = 'blog/post.html'
    # model = Post
    # context_object_data = 'post'
    queryset = Post.objects.all()

    def get_success_url(self):
        return self.request.path

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)

    # def get_context_data(self, **kwargs):
    #     # print(self.object.pk)
    #     context = super().get_context_data(**kwargs)
    #     # post = kwargs.get("object")
    #     # new_reply = None
    #     # context['post'] = post
    #     # context['new_reply'] = new_reply
    #     # context['reply_form'] = self.form_class()
    #     return context


class PostCreateView(CreateView):
    # permission_required = ('adverts.add_post',)
    template_name = 'blog/post_create.html'
    form_class = PostForm
    success_url = '/blog/'


class PostUpdateView(UpdateView):
    # permission_required = ('adverts.change_post',)
    template_name = 'blog/post_create.html'
    form_class = PostForm
    success_url = '/blog/'

    # метод get_object мы используем вместо queryset, чтобы получить информацию
    # об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):
    template_name = 'blog/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/blog/'

