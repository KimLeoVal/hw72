from django.db import models

# Create your models here.
class Quote(models.Model):
    text=models.TextField(max_length=300,verbose_name="Текс")
    name=models.CharField(max_length=100,verbose_name="Автор")
    email=models.EmailField(verbose_name="Почта")
    rate=models.IntegerField(default=0,verbose_name="Рейтинг")
    status=models.BooleanField(default=0,verbose_name="Модерированная")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")




