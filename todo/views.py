from rest_framework.response import Response
from rest_framework import generics, permissions, status
from rest_framework.exceptions import PermissionDenied
from .models import Todo
from .serializers import TodoSerializer
from authenticate.permissions import IsAdmin

class TodoListView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

class TodoDetailUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]  # Only users with the role 'Admin' can update or delete todo items

    def handle_exception(self, exc):
        if isinstance(exc, PermissionDenied):
            return Response({"detail": "You do not have permission to perform this action."}, status=status.HTTP_401_UNAUTHORIZED)
        return super().handle_exception(exc)

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

class TodoCreateView(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]  # Only users with the role 'Admin' can create todo items

    def handle_exception(self, exc):
        if isinstance(exc, PermissionDenied):
            return Response({"detail": "You do not have permission to perform this action."}, status=status.HTTP_401_UNAUTHORIZED)
        return super().handle_exception(exc)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
