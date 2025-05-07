from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User

from rest_framework.permissions import AllowAny,IsAuthenticated

from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import PersonalInfo, Education, Skill, Project
from .serializers import PersonalInfoSerializer, EducationSerializer, SkillSerializer, ProjectSerializer
# Create your views here.
class PersonalInfoListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        personalInfo = PersonalInfo.objects.filter(user=request.user)
        serializer = PersonalInfoSerializer(personalInfo, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        personal_info_data = request.data
        instance, created = PersonalInfo.objects.update_or_create(
            user=request.user,
            defaults=personal_info_data
            )
        serializer = PersonalInfoSerializer(instance)
        return Response(serializer.data, status= 201 if created else 200)
    
class PersonalInfoDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk,user):
        personalinfo=get_object_or_404(PersonalInfo, pk=pk)
        if personalinfo.user != user:
            raise PermissionDenied(" You do not have permission to access this personal info.")
        return personalinfo

    def get(self, request, pk):
        personalInfo = self.get_object(pk,request.user)
        serializer = PersonalInfoSerializer(personalInfo)
        return Response(serializer.data, status=200)
    
    def delete(self, request, pk):
        personalInfo = self.get_object(pk,request.user)
        personalInfo.delete()
        return Response(status=204)
    
    def patch(self, request, pk):
        personalInfo = self.get_object(pk,request.user)
        serializer = PersonalInfoSerializer(personalInfo, data=request.data,partial=True )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
class EducationListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        education = Education.objects.filter(user=request.user)
        serializer = EducationSerializer(education, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = EducationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class EducationDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk,user):
        education=get_object_or_404(Education, pk=pk)
        if education.user != user:
            raise PermissionDenied(" You do not have permission to access this education.")
        return education

    def get(self, request, pk):
        education = self.get_object(pk,request.user)
        serializer = EducationSerializer(education)
        return Response(serializer.data, status=200)
    
    def delete(self, request, pk):
        education = self.get_object(pk,request.user)
        education.delete()
        return Response(status=204)
    
    def patch(self, request, pk):
        education = self.get_object(pk,request.user)
        serializer = EducationSerializer(education, data=request.data,partial=True )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class SkillListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        skill = Skill.objects.filter(user=request.user)
        serializer = SkillSerializer(skill, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = SkillSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class SkillDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk,user):
        skill=get_object_or_404(Skill, pk=pk)
        if skill.user != user:
            raise PermissionDenied(" You do not have permission to access this skill.")
        return skill

    def get(self, request, pk):
        skill = self.get_object(pk,request.user)
        serializer = SkillSerializer(skill)
        return Response(serializer.data, status=200)
    
    def delete(self, request, pk):
        skill = self.get_object(pk,request.user)
        skill.delete()
        return Response(status=204)
    
    def patch(self, request, pk):
        skill = self.get_object(pk,request.user)
        serializer = SkillSerializer(skill, data=request.data,partial=True )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
class ProjectListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        project = Project.objects.filter(user=request.user)
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = ProjectSerializer(data=request.data , context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class ProjectDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk,user):
        project=get_object_or_404(Project, pk=pk)
        if project.user != user:
            raise PermissionDenied(" You do not have permission to access this project.")
        return project
    
    def get(self, request, pk):
        project = self.get_object(pk,request.user)
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=200)
    def delete(self, request, pk):
        project = self.get_object(pk,request.user)
        project.delete()
        return Response(status=204)
    def patch(self, request, pk):
        project = self.get_object(pk,request.user)
        serializer = ProjectSerializer(project, data=request.data,partial=True )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
class SignUpView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            validate_password(password)
        except ValidationError as err:
            return Response({'error': err.messages}, status=400)

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        tokens = RefreshToken.for_user(user)
        return Response(
            {
                'refresh': str(tokens),
                'access': str(tokens.access_token)
            },
            status=201
        )