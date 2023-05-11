from django.views import generic
from .models import Post, Comment, Like
from .forms import AddPost, AddComment
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse_lazy


def indexView(request): 
    p = Paginator(Post.objects.all().order_by('-start_date'), 4)
    page = request.GET.get('page')
    posts = p.get_page(page)
    context = {
        'posts': posts,
    }
    return render(request, 'forum/index.html', context)


class DetailView(FormMixin ,generic.DetailView):
    model = Post
    template_name = 'forum/detail.html'
    form_class = AddComment
    
    def get_success_url(self):
        return reverse('forum:detail', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['form'] = AddComment(initial={'post': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        post = Post.objects.get(slug=self.object.slug)
        form.instance.post = post
        form.save()
        return super(DetailView, self).form_valid(form)

    def get_queryset(self):
        return super().get_queryset()
        

class DeletePost(generic.DeleteView):
    model = Post
    success_url = "/"
    

class CreatePost(generic.CreateView):
    model = Post
    form_class = AddPost
    template_name = 'forum/add.html'

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)


def like_comment(request):
    user = request.user
    if request.method == 'POST':
        comment_id = request.POST.get('comment_id')
        comment_obj = Comment.objects.get(id=comment_id)

        if user in comment_obj.likes.all():
            comment_obj.likes.remove(user)
        else:
            comment_obj.likes.add(user)

        like, created = Like.objects.get_or_create(user=user, comment_id=comment_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

        like.save()

        data = {
            'value': like.value,
            'likes': comment_obj.likes.all().count()
        }

        return JsonResponse(data, safe=False)
    return HttpResponseRedirect("../{slug}/".format(slug=comment_obj.post.slug))