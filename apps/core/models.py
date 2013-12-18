from django.db import models


class PublishModel(models.Model):
    published_date = models.DateTimeField()
    published = models.BooleanField(default=False)

    class Meta:
        abstract = True