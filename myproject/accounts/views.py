from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    user_data = [{"id": user.id, "username": user.username, "email": user.email} for user in users]
    return Response(user_data)

@api_view(['GET'])
def get_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
        user_data = {"id": user.id, "username": user.username, "email": user.email}
        return Response(user_data)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
