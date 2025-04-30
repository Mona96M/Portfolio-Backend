from django.urls import path
from .views import EducationListCreateView, SkillListCreateView

urlpatterns = [
    path('educations/', EducationListCreateView.as_view(), name='education-list-create'),
    path('skills/', SkillListCreateView.as_view(), name='skill-list-create'),
]