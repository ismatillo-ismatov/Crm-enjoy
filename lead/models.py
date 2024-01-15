from django.contrib.auth.models import User
from django.db import models
from team.models import Team


class Lead(models.Model):
    NEW = 'new'
    CONTACTED = 'contacted'
    INPROGRESS = 'inprogress'
    LOST = 'lost'
    WON = 'won'

    CHOICES_STATUS = (
        (NEW, 'New'),
        (CONTACTED, 'Contacted'),
        (INPROGRESS, 'In progress'),
        (LOST, 'Lost'),
        (WON, 'Won'),
    )

    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

    CHOICES_PRIORITY = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )
    team = models.ForeignKey(Team,related_name='leads',on_delete=models.CASCADE)
    company = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    information = models.TextField()
    confidence = models.IntegerField(blank=True,null=True)
    esdimated_value = models.IntegerField(blank=True,null=True)
    status = models.CharField(max_length=25,choices=CHOICES_STATUS,default=NEW)
    priority = models.CharField(max_length=25,choices=CHOICES_PRIORITY,default=MEDIUM)
    created_by = models.ForeignKey(User,related_name='leads',on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company

