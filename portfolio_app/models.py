from django.db import models

# Create your models here.

class Education(models.Model):
    university = models.CharField(max_length=50)
    major = models.CharField(max_length=50)

    def __str__(self):
        return self.university