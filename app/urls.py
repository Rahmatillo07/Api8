import rest_framework
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from .views import (LoginApiView, RegisterApiView, LikeApiView, PostApiView, CommentApiView,)

urlpatterns = [
    path('api/v1/likes/', LikeApiView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/like/<int:pk>/', LikeApiView.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'})),
    path('api/v1/posts/', PostApiView.as_view({'get': 'list', 'post': 'create'}), name='posts'),
    path('api/v1/post/<int:pk>/', PostApiView.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'})),
    path('api/v1/comments/', CommentApiView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/comment/<int:pk>/', CommentApiView.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'})),

    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/register/', RegisterApiView.as_view()),
    path('api/v1/login/', LoginApiView.as_view(),name='login'),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]
