from django.db import models


class History(models.Model):
    email = models.EmailField(verbose_name='е-пошта')
    type_object = models.CharField(max_length=10, verbose_name='обєкт пошуку')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публікації')

    class Meta:
        verbose_name = 'Історія пошуку'
        verbose_name_plural = 'Історія пошуку'
        ordering = ['-published']
