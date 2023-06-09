from django.db import models
from django.utils import timezone
from user.models import Person



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Comments(models.Model):
    message = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    

    

