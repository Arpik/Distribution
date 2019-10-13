from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 100)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    author = models.ForeignKey()
    

