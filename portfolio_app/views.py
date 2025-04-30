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