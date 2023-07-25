from rest_framework.viewsets import ModelViewSet

from courses.models import Course
from courses.serializers import CourseSerializer


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()