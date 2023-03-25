from .models import Todo
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import TodoSerializer

#ステータスコード
#200 OK
#201 Created
#204 No Content
#400 Bad Request
#401 Unauthorized 認証
#403 Forbidden 認可
#404 Not Found
#405 Method Not Allowed
#500 Internal Server Error


class TodoView(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        #many=Trueは複数のデータを返すときに使う
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True) #raise_exception=Trueはエラーがあったら例外を発生させる
        serializer.save()
        return Response(status=201)

class TodoDetailView(APIView):
    def get(self, request, id):
        todo = get_object_or_404(Todo, id=id)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    
    def put(self, request, id):
        todo = get_object_or_404(Todo, id=id)
        serializer = TodoSerializer(todo, data=request.data)
        serializer.is_valid(raise_exception=True)
        # partial=Trueは必須項目以外の項目を更新しないときに使う
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        todo = get_object_or_404(Todo, id=id)  # 本当は例外処理を書く必要があります
        todo.delete()
        return Response(status=204)
