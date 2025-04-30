from django.urls import path
from .views import EducationListCreateView, SkillListCreateView, SkillDetailView

urlpatterns = [
    path('educations/', EducationListCreateView.as_view(), name='education-list-create'),
    path('skills/', SkillListCreateView.as_view(), name='skill-list-create'),
    path('skills/<int:pk>/', SkillDetailView.as_view(), name='skill-detail'),
]