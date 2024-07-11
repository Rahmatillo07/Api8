from django.db import models
from django.contrib.auth.models import User





class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='post')
    content = models.TextField()
    created = models.DateField()

    def __str__(self):
        return self.title


class Like(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    like = models.BooleanField()

    def __str__(self):
        return self.like


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user
