from django.shortcuts import render
from django.http import HttpResponse
#from django.contrib.auth.models import Tutor
from rest_framework import generics
from rest_framework.generics import CreateAPIView
from searchtutor.serializers import TutorSerializer
from searchtutor.serializers import StudentSerializer
from searchtutor.serializers import SubjectSerializer
from searchtutor.models import Tutor
from searchtutor.models import Student
from searchtutor.models import Subject

from rest_framework import filters

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from searchtutor.serializers import RegistrationSerializer
from rest_framework.permissions import IsAuthenticated



def homePageView(request):
    return HttpResponse('Hello, World!')

class TutorregCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer



class StudentregCreate(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class SubjectCreate(generics.CreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['subject_name','tutor__tutor_first_name']

class CustomSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        if request.query_params.get('title_only'):
            return ['title']
        return super(CustomSearchFilter, self).get_search_fields(view, request)

@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            Tutor=serializer.save()
            data['response']= "successfully registered"
        else:
            data=serializer.errors
        return Response(data)