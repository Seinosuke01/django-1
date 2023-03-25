from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    completed = models.BooleanField(default=False)
    # integerfieldは整数を入れる
    priority = models.IntegerField()
    dueDate = models.DateTimeField(blank=True, null=True)
    # auto_now_addは作成した日時を自動で入れてくれる

    def __str__(self):
        return self.title

    # __str__は文字列を返すメソッドselfは自分自身を指す

class Tag(models.Model):
    name = models.CharField(max_length=100)
    # tagとtodoを紐付ける、ManyToManyFieldは複数のデータを紐付ける、related_nameは逆参照するときに使う
    todo = models.ManyToManyField(Todo, related_name="hoge")
    # hogeが謎

    def __str__(self):
        return self.name