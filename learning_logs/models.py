from tabnanny import verbose
from tarfile import data_filter
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    """topic user is learning"""
    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """return a string of the model"""
        return self.text
    
class Entry(models.Model):
    """entry to write something about the topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """returns the entry as a string"""
        return f"{self.text[0:50]}..."
    
