from django.db import models


class PublishModel(models.Model):
    published = models.BooleanField(default=False)

    class Meta:
        abstract = True