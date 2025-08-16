# blog/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # --- Auth ---
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),

    # --- Posts ---
    path("posts/", views.PostListView.as_view(), name="post_list"),
    path("post/new/", views.PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post_delete"),

    # --- Comments ---
    path("post/<int:pk>/comments/new/", views.CommentCreateView.as_view(), name="comment_create"),
    path("comment/<int:pk>/update/", views.CommentUpdateView.as_view(), name="comment_update"),
    path("comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment_delete"),

    # --- Search & Tags ---
    path("search/", views.SearchView.as_view(), name="search"),
    path("tags/<str:tag_name>/", views.TagView.as_view(), name="tag_posts"),

    path("tags/<slug:tag_slug>/", views.PostByTagListView.as_view(), name="tag_posts"),
]
