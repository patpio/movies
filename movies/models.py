from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    actors = models.ManyToManyField('People', related_name='peoples')
    type = models.ManyToManyField('Category', related_name='categories')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class People(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, default='', blank=True)

    class Meta:
        verbose_name_plural = 'People'

    def __str__(self):
        return f'{self.name} {self.surname}'


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
