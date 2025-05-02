from django.contrib import admin
from .models import PersonalInfo,Education,Skill,Project
# Register your models here.
admin.site.register(PersonalInfo)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Project)
