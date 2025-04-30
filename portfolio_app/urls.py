from django.urls import path
from .views import EducationListCreateView

urlpatterns = [
    path('educations/', EducationListCreateView.as_view(), name='education-list-create')
]