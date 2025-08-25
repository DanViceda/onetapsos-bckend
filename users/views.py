# users/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from django.shortcuts import render
from .serializers import UserRegistrationSerializer
from .models import CustomUser

# API view for user registration
class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'message': 'User registered successfully',
                'user_id': user.id
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API view to list all users (JSON response)
class UserListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer

# Django view to render the HTML table
def user_table_view(request):
    return render(request, 'users/user_table.html')

