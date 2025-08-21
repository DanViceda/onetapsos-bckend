# users/urls.py
from django.urls import path
from .views import RegisterView, UserListView, user_table_view

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('user-table/', user_table_view, name='user-table'),
]