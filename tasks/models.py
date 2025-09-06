from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    task_name=models.CharField(max_length=100,null=True)
    task_discription=models.TextField(null=True)
    task_status = models.DateTimeField(null=True,blank=True)




    def __str__(self) -> str:
        return self.task_name