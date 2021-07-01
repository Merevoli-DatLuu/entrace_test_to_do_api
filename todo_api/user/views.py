from django.http import JsonResponse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer

class UserListView(APIView):
    """

    HTTP methods
    -----
    get  ->  API 8

    """
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        """
        [API 8 / GET-ALL-USER]: Get all users
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse({
            'status': 'success',
            'message': 'get all users successfully',
            'data': serializer.data
        }, safe=False)