from django.urls import path

from courses.apps import CoursesConfig
from rest_framework.routers import DefaultRouter

from courses.views import CourseViewSet, PaymentListCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonCreateAPIView, LessonUpdateAPIView, LessonDeleteAPIView

app_name = CoursesConfig.name

router = DefaultRouter()
router.register(prefix=r'courses', viewset=CourseViewSet, basename='courses')

urlpatterns = [
                  # lessons
                  path('lessons/', LessonListAPIView.as_view(), name='lessons_list'),
                  path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_get'),
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
                  path('lesson/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson_update'),
                  path('lesson/<int:pk>/delete/', LessonDeleteAPIView.as_view(), name='lesson_delete'),

                  # payments
                  path('payments/', PaymentListCreateAPIView.as_view(), name='payments_list_create'),
              ] + router.urls
