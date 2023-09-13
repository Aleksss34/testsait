from django.db import models
from django.urls import reverse


class Messager(models.Model):#создание базы данных мессанджер

    title = models.CharField(max_length=255, verbose_name='Заголовок')#вербос смена навзвания таблицы для админки
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True)
    def __str__(self):
        return self.title
    class Meta:#доп класс для изменения названия бд в панели админа
        verbose_name = 'легенда'
        verbose_name_plural = 'легенда'
class Categories(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id':self.pk})
    class Meta:
        verbose_name='категория'
        verbose_name_plural = 'категории'



