from django.db import models
from django.urls import reverse
from uuid import uuid4
from pytils.translit import slugify

class Ingredients(models.Model):
    """Основные классы ингредиентов, из которых создается свеча"""
    name = models.CharField(max_length=150, db_index=True, verbose_name='Ингредиент')
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('Svecha:sostav', args=[self.slug],)


class Product(models.Model):
    """Модель описания составляющих ингредиентов, из которых создается свеча"""
    ingredients = models.ForeignKey(Ingredients, related_name='ingredients', on_delete=models.CASCADE, verbose_name='Ингредиент')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наименование')
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Фото')
    description = models.TextField(blank=True, verbose_name='Описание')
    primechanie = models.TextField(blank=True, verbose_name='Примечание')
    #price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена')
    #available = models.BooleanField(default=True, verbose_name='Наличие')
    #created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Составляющее'
        verbose_name_plural = 'Составляющие'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('Svecha:ingredients_detail', args=[self.id, self.slug,],)

    def save(self, *args, **kwargs):
        """
        Сохранение полей модели при их отсутствии заполнения , например при загрузке из файла
        """
        if not self.slug:
            self.slug = unique_slugify(self, self.name)
        super().save(*args, **kwargs)




def unique_slugify(instance, slug):
    """
    Генератор уникальных SLUG для моделей, в случае существования такого SLUG.,а также автоматическое заполнение если будет пусто, например при загрузке из файла
    """
    model = instance.__class__
    unique_slug = slugify(slug)
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = f'{unique_slug}-{uuid4().hex[:8]}'
    return unique_slug