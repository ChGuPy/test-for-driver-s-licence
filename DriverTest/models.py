# -*- coding:utf-8 -*-
from __future__ import unicode_literals
import PIL
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def saving_path(instance, name):
    return 'image/%s/%s' % (instance.id, name)

class Answer(models.Model):
   answer = models.TextField(verbose_name=u'Вариант ответа', max_length=300, blank=True)
   true = ((True, u'Верный', ),
           (False, u'Неверный', ))
   true_or_false = models.BooleanField(verbose_name=u'Верный ответ?', max_length=5, choices=true, default=False)

   def __unicode__(self):
       return '%s' % self.answer


class Question(models.Model):
    title = models.TextField(verbose_name=u'Вопрос', max_length=300)
    img = models.ImageField(verbose_name=u'Изображение', blank=True, upload_to=saving_path)
    is_active = models.BooleanField(default=True, verbose_name=u'Актуален')
    answer1 = models.ForeignKey(Answer, verbose_name=u'Ответ', related_name='question1', blank=True, null=True)
    answer2 = models.ForeignKey(Answer, verbose_name=u'Ответ', related_name='question2', blank=True, null=True)
    answer3 = models.ForeignKey(Answer, verbose_name=u'Ответ', related_name='question3', blank=True, null=True)
    answer4 = models.ForeignKey(Answer, verbose_name=u'Ответ', related_name='question4', blank=True, null=True)

    def __unicode__(self):
        return '%s' % self.title


class CompleteTest(models.Model):
    user = models.ForeignKey(User, verbose_name=u'Логин пользователя', related_name='login')
    right_answers = models.IntegerField(verbose_name=u'Количество верных ответов', default=0)

    def __unicode__(self):
        return '%s' % self.user



