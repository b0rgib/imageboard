from django.db import models
from django.dispatch import receiver
import os


class PostNumber(models.Model):
    def __str__(self):
        return str(self.id)


class Threads(models.Model):
    number = models.ForeignKey(PostNumber, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default='Аноним')
    head = models.CharField(max_length=30)
    text = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    ref = models.CharField(max_length=1000, default='')
    update = models.IntegerField()
    media = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.name


class Message(models.Model):
    number = models.ForeignKey(PostNumber, on_delete=models.CASCADE)
    thread = models.ForeignKey(Threads, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default='Аноним')
    text = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    ref = models.CharField(max_length=1000, default='')
    sage = models.BooleanField(default=False)
    media = models.ImageField(null=True, blank=True, upload_to='images/')

    class Meta():
        ordering = ['id']

    def __str__(self):
        return self.text


@receiver(models.signals.post_delete, sender=Threads)
@receiver(models.signals.post_delete, sender=Message)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.media:
        if os.path.isfile(instance.media.path):
            os.remove(instance.media.path)
