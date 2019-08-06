from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    
    def __str__(self):
        return self.title