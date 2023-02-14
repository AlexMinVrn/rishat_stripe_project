from django.db import models


class Item(models.Model):
    name = models.CharField('Название товара', max_length=200)
    description = models.TextField('Описание товара', max_length=2000)
    price = models.DecimalField('Цена', max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
