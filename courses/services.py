from config.settings import STRIPE_SECRET_KEY, STRIPE_URL
import requests
from courses.models import Payment


def checkout_session(course, user):
    headers = {'Authorization': f'Bearer {STRIPE_SECRET_KEY}'}
    data = [
        ('amount', course.price),
        ('currency', 'usd'),
    ]
    response = requests.post(STRIPE_URL, headers=headers, data=data)
    if response.status_code != 200:
        raise Exception(f'ошибка : {response.json()["error"]["message"]}')
    return response.json()


def create_payment(course, user):
    Payment.objects.create(
        user=user,
        course=course,
        payment_summ=course.price,
    )
