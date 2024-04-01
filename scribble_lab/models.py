from django.db import models

# Create your models here.

class Post(models.Model):
  author = models.CharField(max_length=40)
  title = models.CharField(max_length=40)
  body = models.CharField(max_length=40)

  def __str__(self):
    return self.author


# class Comment(models.Model):
#   author = models.CharField(max_length=40)
#   body = models.CharField(max_length=40)
#   post = models.ManyToManyField(Post)

#   def __str__(self):
#     return self.author
  
class Comment(models.Model):
  author = models.CharField(max_length=40)
  body = models.CharField(max_length=40)
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts')

  def __str__(self):
    return self.author
