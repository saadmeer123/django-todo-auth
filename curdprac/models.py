from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    STATUS_CHOICE = (
        ('Pending','Pending'),
        ('In Progress','In Progress'),
        ('Completed', 'Completed')
    )

    title = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='Pending')
    deadline = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,  null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.status}"