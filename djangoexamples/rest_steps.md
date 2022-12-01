pip install django_rest_framework

settings.py (project directory)
'rest_framework'

models.py
from django.db import models
class Book(models.Model):
    booktitle = models.CharField(max_length=50)
    bookauthor = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.booktitle},{self.bookauthor}"

serializers.py

from dataclasses import fields
from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
	booktitle = serializers.CharField(max_length=50)
	booktitle = serializers.CharField(max_length=50)
        class Meta:
	   fields = ('__all__')


views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class BookViews(APIView):
    def get(self, request, id=None):
        if id:
            item = Book.objects.get(id=id)
            serializer = BookSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Book.objects.all()
        serializer = BookSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self,request):
        print(request.data)
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":request.data},status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class BookView(APIView):
def put(self, request, pk=None, format=None):
        # Get the todo to update
        todo_to_update = Todo.objects.get(pk=pk)

        # Pass the instance to update to the serializer, and the data and also partial to the serializer
        # Passing partial will allow us to update without passing the entire Todo object
        serializer = TodoSerializer(instance=todo_to_update,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()

        response.data = {
            'message': 'Todo Updated Successfully',
            'data': serializer.data
        }

        return response


def delete(self, request, pk, format=None):
        todo_to_delete =  Todo.objects.get(pk=pk)

        # delete the todo
        todo_to_delete.delete()

        return Response({
            'message': 'Todo Deleted Successfully'
        })


urls.py

urlpatterns = [
        path('todo', TodoAPIView.as_view()),
        path('todo/<str:pk>', TodoAPIView.as_view()) # to capture our ids
    ]






