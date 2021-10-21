from django.db import models


class MemberModel(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    reg = models.CharField(max_length=20)
    course = models.CharField(max_length=20)
    year = models.FloatField()


