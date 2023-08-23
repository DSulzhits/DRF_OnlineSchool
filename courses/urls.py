from django.urls import path

from courses.apps import CoursesConfig
from rest_framework.routers import DefaultRouter

from courses.views import CourseViewSet, PaymentListView, PaymentCreateAPIView, LessonListAPIView, \
    LessonRetrieveAPIView, \
    LessonCreateAPIView, LessonUpdateAPIView, LessonDeleteAPIView, PaymentGetView, SubscriptionCreateAPIView, \
    SubscriptionUpdateView

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
                  path('payments/', PaymentListView.as_view(), name='payments_list'),
                  path('payment/create/', PaymentCreateAPIView.as_view(), name='payment_create'),
                  path('payment/<str:payment_id>/', PaymentGetView.as_view(), name='payment_get'),

                  # subscription
                  path('subscription/create/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
                  path('subscription/<int:pk>/update/', SubscriptionUpdateView.as_view(), name='subscription_update'),
              ] + router.urls
