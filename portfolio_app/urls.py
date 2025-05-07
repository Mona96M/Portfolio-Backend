from django.urls import path
from .views import (PersonalInfoListCreateView,
                    PersonalInfoDetailView,
                    EducationListCreateView,
                    EducationDetailView,
                    SkillListCreateView, 
                    SkillDetailView,
                    ProjectListCreateView,
                    ProjectDetailView,
                    SignUpView,
                    )
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('personalinfo/', PersonalInfoListCreateView.as_view(), name='personalinfo-list-create'),
    path('personalinfo/<int:pk>/', PersonalInfoDetailView.as_view(), name='personalinfo-detail'),
    path('educations/', EducationListCreateView.as_view(), name='education-list-create'),
    path('educations/<int:pk>/', EducationDetailView.as_view(), name='education-detail'),
    path('skills/', SkillListCreateView.as_view(), name='skill-list-create'),
    path('skills/<int:pk>/', SkillDetailView.as_view(), name='skill-detail'),
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    

]