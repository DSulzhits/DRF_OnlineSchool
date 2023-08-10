from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView, \
    CreateAPIView, UpdateAPIView, DestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from courses.models import Course, Lesson, Payment
from users.models import UserRoles
from courses.permissions import IsModerator, IsOwner, IsMember
from courses.serializers import CourseSerializer, LessonSerializer, PaymentsSerializer, LessonListSerializer


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.role == UserRoles.MODERATOR:
            return Course.objects.all()
        else:
            return Course.objects.filter(owner=user)


class LessonListAPIView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.role == UserRoles.MODERATOR:
            return Lesson.objects.all()
        else:
            return Lesson.objects.filter(owner=user)


class LessonRetrieveAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner | IsAdminUser]


class LessonCreateAPIView(CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsMember | IsAdminUser]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonUpdateAPIView(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser | IsModerator | IsOwner]


class LessonDeleteAPIView(DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsAdminUser]


class PaymentListCreateAPIView(ListCreateAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['course', 'lesson', 'payment_type']
    ordering_fields = ['payment_date']
    permission_classes = [IsAuthenticated]

# class LessonListCreateAPIView(ListCreateAPIView):
#     serializer_class = LessonSerializer
#     queryset = Lesson.objects.all()
#     permission_classes = [IsAuthenticated]
#
#     def perform_create(self, serializer):
#         new_lesson = serializer.save()
#         new_lesson.owner = self.request.user
#         new_lesson.save()
#
#
# class LessonRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     serializer_class = LessonSerializer
#     queryset = Lesson.objects.all()
#     permission_classes = [IsAuthenticated]
#
#     def retrieve(self, request, *args, **kwargs):
#         user = self.request.user
#         if user.role == "moderator" or user.is_superuser or ....:
#             return super().retrieve(request, *args, **kwargs)
