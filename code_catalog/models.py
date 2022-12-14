from django.db import models

from config.settings.common import AUTH_USER_MODEL


class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + ' : ' + self.name


class Snippet(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    language = models.CharField(max_length=100)
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return str(self.id) + ' : ' + self.title
