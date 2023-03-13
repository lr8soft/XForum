from django.db import models
from django.utils import timezone

from common import PermissionUtils
from user_manager.models import User


# Create your models here.
class Topic(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    currentfloor = models.IntegerField(default=0)
    repliesCount = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "id:" + self.id + " title:" + self.title + " author:" + self.author + " reoliescount:" + self.repliesCount


class Reply(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.TextField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=False)
    floor = models.IntegerField(null=False)

    def __str__(self):
        return "id:" + self.id + " article:" + self.article + " author:" + self.author + " floor:" + self.floor