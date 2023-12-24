from rest_framework import serializers
from . models import Todo

class TodoSeriazlizer(serializers.ModelSerializer):
    class Meta:
        models = Todo
        fields = ['todo_title']