from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Task, FinishedTask
from .serializers import TaskSerializer, FinishedTaskSerializer
import datetime






class TaskList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        tasks = Task.objects.filter(user=request.user, completed=False)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        # Associate the task with the authenticated user
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request):
        try:
            task_id = request.data.get('task_id')  # Get the task_id from the request data
            task = Task.objects.get(id=task_id, user=request.user, completed=False)
            task.completed = True
            task.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class FinishedTaskList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        finished_tasks = FinishedTask.objects.filter(user=request.user)
        serializer = FinishedTaskSerializer(finished_tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Associate the task with the authenticated user
        data = request.data.copy()
        data['user'] = request.user.id
        
        # Add current time
        data['time'] = datetime.datetime.now().time().strftime('%H:%M:%S')
        
        serializer = FinishedTaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


