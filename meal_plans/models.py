from django.db import models


class Meals(models.Model):

    name = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name