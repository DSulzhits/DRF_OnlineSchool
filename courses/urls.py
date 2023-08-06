from django.urls import path

from courses.apps import CoursesConfig
from rest_framework.routers import DefaultRouter

from courses.views import CourseViewSet, LessonListCreateAPIView, LessonRetrieveUpdateDestroyAPIView, \
    PaymentListCreateAPIView

app_name = CoursesConfig.name

router = DefaultRouter()
router.register(prefix=r'courses', viewset=CourseViewSet, basename='courses')

urlpatterns = [
                  # lessons
                  path('lessons/', LessonListCreateAPIView.as_view(), name='lessons_list_create'),
                  path('lessons/<int:pk>/', LessonRetrieveUpdateDestroyAPIView.as_view(),
                       name='lessons_get_update_delete'),

                  # payments
                  path('payments/', PaymentListCreateAPIView.as_view(), name='payments_list_create'),
              ] + router.urls
