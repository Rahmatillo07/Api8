from django.contrib.auth import authenticate, logout
from django.shortcuts import redirect
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, Post, Like, Comment
from .serializers import LikeSerializer, PostSerializer, CommentSerializer, LoginSerializer, RegisterSerializer
from .permissions import AdminRequiredPermission


from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication, BasicAuthentication


class LoginApiView(ObtainAuthToken):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        return Response({'message': 'Saytga kirish uchun Login va Parolingizni kiriting!'})

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })


class RegisterApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        return Response({'message': 'Assalomu alaykum yangi akkaunt ochish uchun shu formani toldiring'})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_user = User(
            username=serializer.validated_data['username'],
            first_name=serializer.validated_data['first_name'],
            last_name=serializer.validated_data['last_name'],
            password=serializer.validated_data['password']
        )
        new_user.set_password(serializer.validated_data['password'])
        new_user.save()
        return redirect('login')


class LikeApiView(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [AdminRequiredPermission]
    authentication_classes = [TokenAuthentication]


class PostApiView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AdminRequiredPermission]
    authentication_classes = [BasicAuthentication]


class CommentApiView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AdminRequiredPermission]
    authentication_classes = [TokenAuthentication]
