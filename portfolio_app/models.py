from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='educations')
    university = models.CharField(max_length=50)
    major = models.CharField(max_length=50)

    def __str__(self):
        return self.university
    

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')
    name_of_skill = models.CharField(max_length=50)

    def __str__(self):
        return self.name_of_skill
    

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    project_name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    project_url = models.URLField(blank=True) 

    def __str__(self):
        return self.project_name