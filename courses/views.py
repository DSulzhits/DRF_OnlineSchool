from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from courses.models import Course, Lesson
from courses.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonListCreateAPIView(ListCreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

# class LessonCreateAPIView(CreateAPIView):
#     serializer_class = LessonSerializer
#
#
# class LessonListAPIView(ListAPIView):
#     serializer_class = LessonSerializer
#     queryset = Lesson.objects.all()
#
#
# class LessonRetrieveAPIView(RetrieveAPIView):
#     serializer_class = LessonSerializer
#     queryset = Lesson.objects.all()
#
#
# class LessonUpdateAPIView(UpdateAPIView):
#     serializer_class = LessonSerializer
#     queryset = Lesson.objects.all()
#
#
# class LessonDestroyAPIView(DestroyAPIView):
#     queryset = Lesson.objects.all()
