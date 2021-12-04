from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    name = models.CharField(max_length=20)
    phone = PhoneNumberField()
    message = models.TextField()

    def __str__(self):
        return self.name


class CategoryPortfolio(models.Model):
    name = models.CharField('Категория', max_length=30)
    slug = models.SlugField('URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория портфолио'
        verbose_name_plural = 'Категории портфолио'


class Portfolio(models.Model):
    title = models.CharField('Название', max_length=30)
    small_image = models.ImageField('Маленькая картинка', upload_to='static/image')
    large_image = models.ImageField('Большая картинка', upload_to='static/image')
    cat = models.ForeignKey('CategoryPortfolio', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'
