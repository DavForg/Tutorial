import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
	def was_published_recently(self):
		question_text = models.CharField(max_length=200)
		pub_date = models.DateTimeField('date published')
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
	def __str__(self):
		question = models.ForeignKey(Question)
		choice_text = models.CharField(max_length=200)
		votes = models.IntegerField(default=0)# __unicode__ on Python 2
		return self.choice_text
