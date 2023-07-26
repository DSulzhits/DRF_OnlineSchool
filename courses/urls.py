from django.urls import path

from courses.apps import CoursesConfig
from rest_framework.routers import DefaultRouter

from courses.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView

app_name = CoursesConfig.name

router = DefaultRouter()
router.register(prefix=r'courses', viewset=CourseViewSet, basename='courses')

urlpatterns = [
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
                  path('lessons/', LessonListAPIView.as_view(), name='lessons_list'),
                  path('lesson/<int:pk>', LessonRetrieveAPIView.as_view(), name='lesson_get'),
                  path('lesson/<int:pk>/update', LessonUpdateAPIView.as_view(), name='lesson_update'),
                  path('lesson/<int:pk>/delete', LessonDestroyAPIView.as_view(), name='lesson_delete'),
              ] + router.urls
