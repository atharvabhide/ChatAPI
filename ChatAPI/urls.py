from django.contrib import admin
from django.urls import path, include
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

class ChatAPIView(GenericAPIView):
    permission_classes = []
    authentication_classes = []
    def get(self, request, *args, **kwargs):
        return Response({
            'conversations': 'http://localhost:8000/conversations/',
            'users': 'http://localhost:8000/users/',
            'login': 'http://localhost:8000/auth/login/',
            'logout': 'http://localhost:8000/auth/logout/',
            'register': 'http://localhost:8000/auth/registration/',
            'change_password': 'http://localhost:8000/auth/password/change/',
            'reset_password': 'http://localhost:8000/auth/password/reset/',
            'reset_password_confirm': 'http://localhost:8000/auth/password/reset/confirm/',
            'reset_password_complete': 'http://localhost:8000/auth/password/reset/complete/',
            'reset_password_confirm': 'http://localhost:8000/auth/password/reset/confirm/',
        })

urlpatterns = [
    path('', ChatAPIView.as_view()),
    path('admin/', admin.site.urls),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('conversations/', include('chat.urls')),
    path('users/', include('users.urls'))
]
