# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse
from bs4 import BeautifulSoup


@python_2_unicode_compatible
class Standardclass(models.Model):
    name = models.CharField('栏目名称', max_length=20)
    slug = models.CharField('栏目网址', max_length=30, db_index=True, primary_key=True)

    #def get_absolute_url(self):
    #    return reverse('information', args=(self.name, self.slug ))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '其他栏目'
        verbose_name_plural = '其他栏目'
        ordering = ['name']  # 排序


@python_2_unicode_compatible
class Resourcesclass(models.Model):
    name = models.CharField('下载文件类别', max_length=20)
    slug = models.CharField('文件类别网址', max_length=30, db_index=True, primary_key=True)
    intro = models.TextField('类别简介', default='')
    pic = models.ImageField('封面', upload_to="uploads/images/download/")
    browser = models.IntegerField('访问量', default=0, editable=False)

    #def get_absolute_url(self):
    #    return reverse('information', args=(self.name, self.slug ))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '资源下载栏目'
        verbose_name_plural = '资源下载栏目'
        ordering = ['name']  # 排序



@python_2_unicode_compatible
class Standardarticle(models.Model):
    column = models.ForeignKey(Standardclass, verbose_name='归属栏目')
    title = models.CharField('标题', max_length=40)
    source = models.CharField('来源', max_length=20)
    author = models.CharField('作者', max_length=20)
    browser = models.IntegerField('浏览量', default=0, editable=False)
    keyword = models.CharField('关键词', max_length=30, blank=True)
    tag = models.CharField('标签', max_length=30, blank=True)
    content = models.TextField('内容', default='', blank=True)
    content = UEditorField('内容', height=300, width=700,
        default=u'', blank=True, imagePath="uploads/images/article/",
        toolbars='besttome', filePath='uploads/files/article/')
    def fengmian(self):
        html = self.content
        soup = BeautifulSoup(html, "html.parser")
        try:
            picurl = soup.img["src"]
        except:
            picurl = "/media/defaultpic.jpg"
        return picurl
    picurl = property(fengmian)
    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)
    published = models.BooleanField('正式发布', default=True)

    #def get_absolute_url(self):
    #    return reverse('infoarticle', args=(self.pk, self.slug))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '其他'
        verbose_name_plural = '其他'


@python_2_unicode_compatible
class Resourcearticle(models.Model):
    column = models.CharField('下载', default='download', max_length=10, editable=False)
    title = models.CharField('标题', max_length=40)
    source = models.CharField('来源', max_length=20)
    author = models.CharField('作者', max_length=20)
    browser = models.IntegerField('下载量', default=0, editable=False)
    album = models.ForeignKey(Resourcesclass, verbose_name='归属类别')
    filename = models.FileField('上传文件', upload_to='uploads/files/download/')
    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)
    published = models.BooleanField('正式发布', default=True)

    #def get_absolute_url(self):
    #    return reverse('infoarticle', args=(self.pk, self.slug))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '资源下载'
        verbose_name_plural = '资源下载'

@python_2_unicode_compatible
class Lunbopic(models.Model):
    lunbopic = models.ImageField('轮播图片', upload_to='uploads/images/lunbo/')
    url = models.CharField('链接地址', max_length=100, default='')
    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)
    published = models.BooleanField('正式发布', default=True)
    #def get_absolute_url(self):
    #    return reverse('information', args=(self.name, self.slug ))

    def __str__(self):
        return self.lunbopic.name

    class Meta:
        verbose_name = '轮播图片'
        verbose_name_plural = '轮播图片'


