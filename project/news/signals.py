from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Record

from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives


# ф-я выполняться при создании объекта модели Record
@receiver(post_save, sender=Record)
def record_created(instance, **kwargs):
    emails = User.objects.filter(
        subscriptions__category=instance.category
    ).values_list('email', flat=True)

    subject = f'Новая запись в категории {instance.category}'

    text_content = (
        f'Название: {instance.title}\n'
        f'Анонс: {instance.full_text}\n\n'
        f'Ссылка на публикацию: http://127.0.0.1:8000{instance.get_absolute_url()}'
    )
    html_content = (
        f'Название: {instance.title}<br>'
        f'Анонс: {instance.full_text}<br><br>'
        f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
        f'Ссылка на публикацию</a>'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

