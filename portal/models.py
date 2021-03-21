from django.db import models

class Commands(models.Model):
    """
    Класс описывает базовые голосовые команды
    """
    command = models.CharField(max_length=127, verbose_name='Наименование команды')
    description = models.TextField(verbose_name='Описание команды')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

    def __str__(self):
        return self.command