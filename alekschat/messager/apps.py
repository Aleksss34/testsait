from django.apps import AppConfig

#все приложения сайта
class MessagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'messager'
    verbose_name = 'вкладки'#альтернативное название например дляадмин панели
