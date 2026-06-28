from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Task
from .serializers import RegisterSerializer, TaskSerializer
from rest_framework.permissions import IsAuthenticated



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    filterset_fields = ["status"]
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "updated_at"]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Task.objects.all()
    
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Task.objects.all()

        return Task.objects.filter(owner=user)
