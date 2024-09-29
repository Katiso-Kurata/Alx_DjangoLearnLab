# accounts/urls.py

from django.urls import path
from .views import RegisterView, LoginView
from rest_framework import generics, permissions
from .serializers import User, UserRegistrationSerializer
from .views import ProfileView


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user




urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
]

