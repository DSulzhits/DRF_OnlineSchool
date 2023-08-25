from django.conf import settings
from django.core.mail import send_mail
from courses.models import CourseSubscription
from datetime import datetime, timedelta
from celery import shared_task
from users.models import User
from django.utils import timezone


@shared_task
def send_mail_course_update(object_pk):
    subscription_list = CourseSubscription.objects.filter(course=object_pk)
    for subscription in subscription_list:
        send_mail(
            subject="Обновление курса",
            message=f"Курс на который вы подписаны: {subscription}, получил обновление",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[subscription.user.email]
        )


@shared_task
def check_user_last_login():
    current_date = datetime.now()
    date_month_ago = current_date - timedelta(days=30)
    inactive_users = User.objects.filter(last_login=date_month_ago, is_active=True)
    inactive_users.update(is_active=False)
    # print(inactive_users)








