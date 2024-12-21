from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name='Title', max_length=100)
    content = models.TextField(verbose_name='Content')
    date_posted = models.DateTimeField(verbose_name='Date Time Posted', auto_now_add=True)
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('home')
