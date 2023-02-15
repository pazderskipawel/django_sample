from django.db import models

# Create your models here.
class UserTerm(models.Model):
    userId = models.IntegerField()
    term = models.CharField(max_length=500, default='xd')
    def __str__(self):
        return f"{self.term} ({self.userId})"