from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'カテゴリ'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'タグ'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField('タイトル', max_length=70)
    body = models.TextField('本文')
    created_time = models.DateTimeField('作成日時')
    modified_time = models.DateTimeField('修正日時')
    excerpt = models.CharField('概要', max_length=200, blank=True)
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name='タグ', blank=True)
    author = models.ForeignKey(User, verbose_name='筆者', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'コンテンツ'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
