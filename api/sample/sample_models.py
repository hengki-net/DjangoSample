from django.db import models


class sample_Model(models.Model):
    PON = models.CharField(max_length=10, primary_key=True)
    IN_DATE = models.DateTimeField()


