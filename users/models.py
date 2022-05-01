from django.db import models


class Subscribes(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class FeedBack(models.Model):
    name = models.CharField(max_length=56)
    subject = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.IntegerField()
    text = models.TextField()

    def __str__(self):
        return self.name
