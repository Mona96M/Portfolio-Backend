from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Education
from .serializers import EducationSerializer
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