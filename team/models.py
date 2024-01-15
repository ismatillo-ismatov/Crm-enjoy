from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=200)
    members = models.ManyToManyField(User,related_name='teams')
    created_by = models.ForeignKey(User,related_name='created_team',on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name