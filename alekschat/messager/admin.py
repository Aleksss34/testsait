from django.contrib import admin
from .models import *

class MessagerAdmin(admin.ModelAdmin):#добавит ьэтот класс при регистрации основного класса в админке
    list_display = ('id', 'title', 'content', 'time_create', 'photo', 'is_published')#выводит список этих полей в админ панеле
    list_display_links = ('id', 'title')#определяет кликабельные поля
    search_fields = ('title', 'content')#определяет по каким полям можно производит ьпоиск информации
    list_editable = ('content', 'photo', 'is_published')#разрешенные редактировать столбцы
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Messager, MessagerAdmin)#добавления баз данных для администрирования в джанго
admin.site.register(Categories, CategoriesAdmin)