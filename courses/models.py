from django.db import models
from users.models import NULLABLE, User


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='курс')
    preview = models.ImageField(upload_to='courses/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(upload_to='lessons/', verbose_name='превью', **NULLABLE)
    video_url = models.URLField(verbose_name='видео', **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Payment(models.Model):
    CASH = 'наличные'
    TRANSFER = 'перевод'
    PAYMENT_TYPE = [(CASH, 'наличные'), (TRANSFER, 'перевод')]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    payment_date = models.DateField(auto_now_add=True, verbose_name='дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='урок', **NULLABLE)
    payment_summ = models.PositiveIntegerField(verbose_name='сумма оплаты')
    payment_type = models.CharField(choices=PAYMENT_TYPE, max_length=20, default=CASH, verbose_name='способ оплаты')

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

    def __str__(self):
        return f"{self.user} - {self.payment_date}, {self.payment_type}"
