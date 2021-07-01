from django.contrib.auth import authenticate
from django.http import JsonResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .serializers import UserSignUpSerializer, UserSignInSerializer

class UserSignUpView(APIView):
    """

    HTTP methods
    -----
    post  ->  API 1

    """

    def post(self, request):
        """
        [API 1 / SIGN-UP]: Sign up for a new user
        """
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Register successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'status': 'error',
            'message': serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)

class UserSignInView(APIView):
    """

    HTTP methods
    -----
    post  ->  API 2

    """

    def post(self, request):
        """
        [API 2 / SIGN-IN]: Sign in
        """
        serializer = UserSignInSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                request,
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            if user:
                refresh = TokenObtainPairSerializer.get_token(user)
                data = {
                    'refresh_token': str(refresh),
                    'access_token': str(refresh.access_token)
                }

                return JsonResponse({
                    'status': 'success',
                    'message': 'Login successfully',
                    'data': data
                }, status=status.HTTP_200_OK)

            return JsonResponse({
                'status': 'fail',
                'message': 'Email or password is incorrect!'
            }, status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse({
            'status': 'error',
            'message': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)