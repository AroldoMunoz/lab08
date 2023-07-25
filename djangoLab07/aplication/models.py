from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Time(models.Model):
    time = models.CharField(max_length=20)
    temperature = models.CharField(max_length=5)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.time