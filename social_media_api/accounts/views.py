from rest_framework import generics, permissions, status, views
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .serializers import RegisterSerializer

CustomUser = get_user_model()

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    queryset = CustomUser.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

class FollowUserView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, user_id):
        target = get_object_or_404(CustomUser, id=user_id)
        request.user.following.add(target)
        return Response({'detail': 'Followed'})

class UnfollowUserView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, user_id):
        target = get_object_or_404(CustomUser, id=user_id)
        request.user.following.remove(target)
        return Response({'detail': 'Unfollowed'})
