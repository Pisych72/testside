from django.db import models
from django.urls import reverse #для построения абсолютных ссылок
# Create your models here.
class news(models.Model):
    title=models.CharField('Наименование',max_length=150)
    content=models.TextField('Контент',blank=True)
    created_at=models.DateTimeField('Дата создания',auto_now_add=True)
    updated_at=models.DateTimeField('Дата обновления',auto_now=True)
    photo=models.ImageField('Изображение',upload_to='photos/%Y/%m/%d/',blank=True)
    is_published=models.BooleanField('Опубликовано',default=True)
    category=models.ForeignKey('Category',on_delete=models.PROTECT,null=True,verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('view_news',kwargs={'news_id':self.pk})

    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Новость'
        verbose_name_plural = 'Новости'
        ordering=['created_at']

class Category(models.Model):
    title=models.CharField('Наименование категории',max_length=150,db_index=True)

    def get_absolute_url(self):
        return reverse('category',kwargs={'category_id':self.pk})


    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Категория'
        verbose_name_plural = 'Категории'
        ordering=['title']