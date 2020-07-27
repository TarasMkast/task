from django.db import models


class History(models.Model):
    email = models.EmailField(verbose_name='е-пошта')
    type_object = models.CharField(max_length=20, verbose_name='обєкт пошуку')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публікації')

    class Meta:
        verbose_name = 'Історія пошуку'
        verbose_name_plural = 'Історія пошуку'
        ordering = ['-published']


objtypes = (('cafe', 'Cafe'),
            ('hospital', 'Hospital'),
            ('police', 'Police')
            )


class Objtype(models.Model):
    objtype = models.CharField(max_length=20, choices=objtypes)

    def __str__(self):
        return self.objtype

    class Meta:
        verbose_name_plural = 'Типи місця пошуку'
        verbose_name = 'Тип місця пошуку'
        ordering = ['objtype']

