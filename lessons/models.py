from django.db import models
from users.models import NULLABLE


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(upload_to='lessons/', verbose_name='превью', **NULLABLE)
    video_url = models.URLField(verbose_name='видео', **NULLABLE)