'''定义在应用程序中管理的数据,告诉Django如何处理应用程序中储存的数据'''
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    '''
    Topic 的 Docstring
    用户学习的主题
    '''
    text = models.CharField(max_length=150)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        '''返回模型的字符串表示'''
        return self.text

class Entry(models.Model):
    '''学到的有关某个主题的具体知识'''
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        '''返回一个表示条目的简单字符串'''
        return f'{self.text[:50]}...'