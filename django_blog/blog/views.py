from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.db.models import Q

from .forms import RegisterForm, ProfileForm, PostForm, CommentForm
from .models import Post, Comment

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created. Welcome!")
            return redirect("post_list")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})

@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect("profile")
    else:
        form = ProfileForm(instance=request.user)
    return render(request, "blog/profile.html", {"form": form})

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 10

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["comment_form"] = CommentForm()
        return ctx

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Post created.")
        return super().form_valid(form)

class IsAuthorMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def test_func(self):
        return self.get_object().author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")

    def test_func(self):
        return self.get_object().author == self.request.user

class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                post=post,
                author=request.user,
                content=form.cleaned_data["content"]
            )
            messages.success(request, "Comment added.")
        return redirect(post.get_absolute_url())
        
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def test_func(self):
        return self.get_object().author == self.request.user

    def get_success_url(self):
        return self.object.post.get_absolute_url()

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "blog/comment_confirm_delete.html"

    def test_func(self):
        return self.get_object().author == self.request.user

    def get_success_url(self):
        return self.object.post.get_absolute_url()

class SearchView(ListView):
    model = Post
    template_name = "blog/search_results.html"
    context_object_name = "results"
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get("q", "").strip()
        qs = Post.objects.all()
        if q:
            qs = qs.filter(
                Q(title__icontains=q) |
                Q(content__icontains=q) |
                Q(tags__name__icontains=q)
            ).distinct()
        return qs

class TagView(ListView):
    model = Post
    template_name = "blog/tag_results.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        tag_name = self.kwargs["tag_name"]
        return Post.objects.filter(tags__name=tag_name)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["tag_name"] = self.kwargs["tag_name"]
        return ctx
class PostByTagListView(ListView):
    model = Post
    template_name = "blog/tag_results.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        tag_slug = self.kwargs.get("tag_slug")
        return Post.objects.filter(tags__slug=tag_slug)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["tag_slug"] = self.kwargs.get("tag_slug")
        return ctx
