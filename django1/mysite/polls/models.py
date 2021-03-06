import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):#tên gọi của đối tượng
        return self.question_text+"+"+str(self.pub_date)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    describe = models.CharField(max_length=100, null=True)
    # mặc định "choice_set" là name quản lý sự liên quan giữa Question và Choice,thay đổi bằng related_name

    def __str__(self):
        return self.choice_text+" + "+str(self.votes)+"+ id:"+str(self.id)

class test(models.Model):
    name= models.CharField(max_length=100)
    content =models.CharField(max_length=100)
    create =models.DateTimeField(datetime.datetime.now(), null=True)

    def __str__(self):
        return self.name