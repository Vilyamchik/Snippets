from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

LANGS = (
    ('py', 'Python'),
    ('js', 'JavaScript'),
    ('cpp', 'C++')
)

class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=30)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE,blank=True, null=True)
    public = models.BooleanField(default=True)
    
    def __repr__(self) -> str:
        return f'Snippet({self.name})'
    

class Comment(models.Model):
    text = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    snippet = models.ForeignKey('Snippet', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Comment  {self.author.username} {self.creation_date}'
    

