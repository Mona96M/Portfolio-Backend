from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User

from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from .models import Education, Skill
from .serializers import EducationSerializer, SkillSerializer
# Create your views here.

class EducationListCreateView(APIView):
    def get(self, request):
        education = Education.objects.all()
        serializer = EducationSerializer(education, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = EducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

class SkillListCreateView(APIView):
    def get(self, request):
        skill = Skill.objects.filter(user=request.user)
        serializer = SkillSerializer(skill, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class SkillDetailView(APIView):
    def get_object(self, pk, user):
        skill = get_object_or_404(skill, pk=pk)
        if skill.user != user:
            raise PermissionDenied(" You don't have permission to access this skill.")
        return skill

    def get(self, request, pk):
        skill = self.get_object(pk, request.user)
        serializer = SkillSerializer(skill)
        return Response(serializer.data, status=200)
    
    def delete(self, request, pk):
        skill = self.get_object(pk, request.user)
        skill.delete()
        return Response(status=204)