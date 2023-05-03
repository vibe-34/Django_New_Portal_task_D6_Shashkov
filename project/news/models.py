from django.db import models


class Record(models.Model):  # Класс публикации
    title = models.CharField('Название', max_length=64)
    full_text = models.TextField('Статья')
    data = models.DateTimeField('Дата публикации')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:                       # Класс для переименования таблицы в админке. Обязательное название класса - Meta
        verbose_name = 'Новость'         # Указываем название таблицы в единственном числе
        verbose_name_plural = 'Новости'  # Указываем название таблицы во множественном числе


class Category(models.Model):
    title = models.CharField(max_length=64, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.title}'
