from django.db import models

# Create your models here.

class Basemodel(models.Model):
    uid = models.UUIDField(primary_key=True,editable=False)
    created_at = models.DateField(auto_created=True)
    updated_at = models.DateField(auto_created=True)

    class Meta:
        abstract = True 

class Todo(Basemodel):
    todo_title = models.CharField(max_length=100)
    todo_decsription = models.TextField()
    is_done = models.BooleanField(default=False)
