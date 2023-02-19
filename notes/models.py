from django.db import models

# Create your models here.
class Note(models.Model):
    userid = models.IntegerField(default='0')
    title = models.CharField(max_length=100)
    date = models.DateField()
    content = models.TextField(default='Notatka...')
    def __str__(self):
        return self.title