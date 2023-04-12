from django.db import models


class Game(models.Model):
    descriptions = models.TextField()
    stageNumber = models.IntegerField()
    date = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return self.descriptions


class User(models.Model):
    name = models.CharField(max_length=255)
    stageOne = models.BooleanField()
    stageTwo = models.BooleanField()

    def __str__(self) -> str:
        return self.name
