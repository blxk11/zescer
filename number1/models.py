from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    skills = models.CharField(max_length=100)

class Jobs(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    is_open = models.BooleanField()

class Application(models.Model):
    candidate = models.ForeignKey(User, on_delete=models.CASCADE)
    jobs = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)