from rest_framework import generics, permissions,status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from posts.models import Post
from posts.serializers import PostSerializer
from .serializers import PublicUserSerializer, RegisterSerializer, UserSerializer
from rest_framework.views import APIView
from django.db.models import Q

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response({"error": "Invalid Credentials"}, status=400)

class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target = generics.get_object_or_404(User, pk=user_id)
        if target == request.user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        # idempotent: add if not exists
        request.user.following.add(target)
        return Response({"detail": f"Now following {target.username}."}, status=status.HTTP_200_OK)

class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target = generics.get_object_or_404(User, pk=user_id)
        if target == request.user:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.remove(target)
        return Response({"detail": f"Unfollowed {target.username}."}, status=status.HTTP_200_OK)

class ListFollowersView(generics.ListAPIView):
    """
    List people who follow <user_id>
    """
    serializer_class = PublicUserSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        user = generics.get_object_or_404(User, pk=self.kwargs['user_id'])
        return user.followers.all()

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['request'] = self.request
        return ctx

class ListFollowingView(generics.ListAPIView):
    """
    List people that <user_id> is following
    """
    serializer_class = PublicUserSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        user = generics.get_object_or_404(User, pk=self.kwargs['user_id'])
        return user.following.all()

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['request'] = self.request
        return ctx
class FeedView(generics.ListAPIView):
    """
    Returns posts from users the authenticated user follows (and optionally themselves).
    Sorted newest first (Post.Meta.ordering handles -created_at).
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_ids = user.following.values_list('id', flat=True)

        include_self = self.request.query_params.get('include_self', 'true').lower() != 'false'
        q = Q(author__in=following_ids)
        if include_self:
            q |= Q(author=user)

        return Post.objects.select_related('author').filter(q)