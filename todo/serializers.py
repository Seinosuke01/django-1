# TodoのModelSerializer

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Todo

"""
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    completed = models.BooleanField(default=False)
    # integerfieldは整数を入れる
    priority = models.IntegerField()
    dueDate = models.DateTimeField(blank=True, null=True)
"""

class TodoSerializer(ModelSerializer):
    title_and_desc = serializers.SerializerMethodField()

    def get_title_and_desc(self, obj):
        return f"{obj.title} - {obj.description}"
    
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long")
        return value
    
    #複数のフィールドをまたがってバリデーションを行う場合はvalidateを使う
    def validate(self, data):
        if data['title'] == data['description']:
            raise serializers.ValidationError("Title and Description must be different")
        return data

    class Meta:
        model = Todo
        fields = "__all__"
        extra_kwargs = {'priority': {'write_only': True}}