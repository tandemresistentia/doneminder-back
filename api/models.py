from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from accounts.models import CustomUser

class Task(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    time = models.TimeField()
    date = models.DateField()
    completed = models.BooleanField(default=False)  

    def __str__(self):
        return self.description
    
class FinishedTask(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    time = models.TimeField()
    date = models.DateField()

    def __str__(self):
        return self.description