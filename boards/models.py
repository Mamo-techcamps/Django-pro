from django.db import models
from django.contrib.auth.models import User    # import user class 

# Create your models here.

class Board(models.Model):
  name = models.CharField(max_length = 50, unique = True)
  description = models.CharField(max_length = 200)

  def __str__(self):
    return self.name

class Topic(models.Model):
  subject = models.CharField(max_length = 200)
  created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name ='topics')
  board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name = 'topics')
  created_dt = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
  message = models.TextField(max_length = 4000)
  topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name = 'posts')
  created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name ='posts')
  created_dt = models.DateTimeField(auto_now_add=True)

