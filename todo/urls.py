from django.urls import path
from .views import TodoListView, TodoDetailUpdateView, TodoCreateView

urlpatterns = [
    path('list/', TodoListView.as_view(), name='todo-list'),
    path('create/', TodoCreateView.as_view(), name='todo-create'),
    path('<int:pk>/', TodoDetailUpdateView.as_view(), name='todo-detail'),
]
