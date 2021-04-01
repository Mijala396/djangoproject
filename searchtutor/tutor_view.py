from rest_framework.generics import ListAPIView

from searchtutor.serializers import TutorSerializer
from searchtutor.models import Tutor

class Tutorlist (ListAPIView):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
