from django.http import JsonResponse, Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import Todo
from django.contrib.auth.models import User
from .serializers import TodoSerializer, TodoAssignSerializer, TodoUpdateSerializer

class TodoListView(APIView):
    """

    HTTP methods
    -----
    get  ->  API 6
    post ->  API 3

    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        """
        [API 6 / GET-ALL-TO-DO]: Get all todos
        """
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return JsonResponse({
            'status': 'success',
            'message': 'get all todos succesfully',
            'data': serializer.data
        }, status=status.HTTP_200_OK, safe=False)

    def post(self, request, format=None):
        """
        [API 3 / ADD-TO-DO]: Add a new todo
        """
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'status': 'success',
                'message': 'add a new todo succesfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return JsonResponse({
            'status': 'error',
            'message': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class TodoDetailView(APIView):
    """

    HTTP methods
    -----
    get     ->  API 7
    post    ->  API 9
    put     ->  API 4
    delete  ->  API 5
    
    """
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        """
        Get a todo object by pk

        :param: pk -> int
        :return: todo.models.Todo

        """
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise Http404

    def get_user(self, user_id):
        """
        Get a user object by user_id

        :param: user_id -> int
        :return: django.contrib.auth.models.User

        """
        try:
            return User.objects.get(pk=user_id)
        except Todo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        [API 7 / GET-TO-DO-BY-ID]: Get a todos detail by id
        """
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo)
        return JsonResponse({
                'status': 'success',
                'message': 'get a todo succesfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)

    def post(self, request, pk):
        """
        [API 9 / ASSIGN-TO-DO]: Assign a todo to specific user
        """
        todo = self.get_object(pk)
        serializer = TodoAssignSerializer(todo, data=request.data)
        if serializer.is_valid():
            assigned_user = self.get_user(serializer.validated_data['user_id'].id)
            if request.user.id == assigned_user.id:     
                return JsonResponse({
                    'status': 'fail',
                    'message': "duplicate assign user"
                }, status=status.HTTP_400_BAD_REQUEST, safe=False)
            
            serializer.save()
            return JsonResponse({
                    'status': 'success',
                    'message': "Assign user successfully"
                }, status=status.HTTP_200_OK, safe=False)

        return JsonResponse({
            'status': 'error',
            'message': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        """
        [API 4 / UPDATE-TO-DO]: Update a todo
        """
        todo = self.get_object(pk)
        if todo.status == "COMPLETE":
            return JsonResponse({
                'status': 'fail',
                'message': "This task is already completed"
            }, status=status.HTTP_400_BAD_REQUEST, safe=False)

        serializer = TodoUpdateSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'status': 'success',
                'message': 'update a todo successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        [API 5 / REMOVE-TO-DO]: Delete a todo
        """
        todo = self.get_object(pk)

        if todo.status == "COMPLETE":
            return JsonResponse({
                'status': 'fail',
                'message': "This task is already completed"
            }, status=status.HTTP_400_BAD_REQUEST, safe=False)

        todo.delete()

        return JsonResponse({
            'status': 'success',
            'message': "Delete task successfully",
        }, status=status.HTTP_200_OK, safe=False)




