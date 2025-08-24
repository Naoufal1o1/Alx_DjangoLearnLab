from rest_framework import viewsets, permissions, decorators, response, status, generics, views
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from notifications.models import Notification

User = get_user_model()

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @decorators.action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            Notification.objects.create(recipient=post.author, actor=request.user, verb='liked your post')
            return response.Response({'detail': 'Liked'}, status=status.HTTP_201_CREATED)
        return response.Response({'detail': 'Already liked'})

    @decorators.action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        post = generics.get_object_or_404(Post, pk=pk)
        Like.objects.filter(user=request.user, post=post).delete()
        return response.Response({'detail': 'Unliked'})

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.request.data.get('post'))
        serializer.save(author=self.request.user, post=post)

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')

class PostLikeView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        Like.objects.get_or_create(user=request.user, post=post)
        return response.Response({'detail': 'Liked'})

class PostUnlikeView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        Like.objects.filter(user=request.user, post=post).delete()
        return response.Response({'detail': 'Unliked'})
