from django.db import models

class HelpList(models.Model):
    name = models.CharField('Commercial name', max_length=1000)
    photo = models.ImageField('Photo', upload_to='photo/%Y/%m/%b')
    data = models.DateField('Date', auto_now_add=True)

    def __str__(self):
        return self.name

class Meta:
    verbose_name = 'My name'
    verbose_name_plural = 'My names'

    
class PromoBlock(models.Model):
    title = models.CharField('Заголовок', max_length=1000)
    description = models.TextField('Описание')
    date_created = models.DateTimeField('Дата создания', auto_now_add=True)
    phototutor = models.ImageField('Photo', upload_to='photo/%Y/%m/%b')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Промо-блок'
        verbose_name_plural = 'Промо-блоки'


class BannerBlock(models.Model):
    title = models.CharField('Заголовок', max_length=1000)
    description = models.TextField('Описание')
    date_created = models.DateTimeField('Дата создания', auto_now_add=True)
    phototutor = models.ImageField('Photo', upload_to='photo/%Y/%m/%b')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Баннер-блок'
        verbose_name_plural = 'Баннер-блоки'

class SponsorBlock(models.Model):
    title = models.CharField('Заголовок', max_length=1000)
    date_created = models.DateTimeField('Дата создания', auto_now_add=True)
    phototutor = models.ImageField('Photo', upload_to='photo/%Y/%m/%b')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Спонсор-блок'
        verbose_name_plural = 'Спонсор-блоки'

class OrderBlock(models.Model):
    title = models.CharField('Заголовок', max_length=1000)
    description = models.TextField('Описание')
    date_created = models.DateTimeField('Дата создания', auto_now_add=True)
    phototutor = models.ImageField('Photo', upload_to='photo/%Y/%m/%b')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заказ-блок'
        verbose_name_plural = 'Заказ-блоков'

class ProductBlock(models.Model):
    title = models.CharField('Заголовок', max_length=1000, default='Без названия')
    date_created = models.DateTimeField('Дата создания', auto_now_add=True)
    phototutor = models.ImageField('Photo', upload_to='photo/%Y/%m/%b')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт-блок'
        verbose_name_plural = 'Продукт-блоки'

class ProductBlock2(models.Model):
    title = models.CharField('Заголовок', max_length=1000, default='Без названия')
    date_created = models.DateTimeField('Дата создания', auto_now_add=True)
    phototutor = models.ImageField('Photo', upload_to='photo/%Y/%m/%b')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт-блок2'
        verbose_name_plural = 'Продукт-блоки2'

class ProductBlock3(models.Model):
    title = models.CharField('Заголовок', max_length=1000, default='Без названия')
    date_created = models.DateTimeField('Дата создания', auto_now_add=True)
    phototutor = models.ImageField('Photo', upload_to='photo/%Y/%m/%b')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт-блок3'
        verbose_name_plural = 'Продукт-блоки3'

class ProductBlock4(models.Model):
    title = models.CharField('Заголовок', max_length=1000, default='Без названия')
    date_created = models.DateTimeField('Дата создания', auto_now_add=True)
    phototutor = models.ImageField('Photo', upload_to='photo/%Y/%m/%b')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт-блок4'
        verbose_name_plural = 'Продукт-блоки4'
# Create your models here.