from django.db import models


class System(models.Model):
    init = models.BooleanField(default=False)
    debug = models.BooleanField(default=False)
    hostname = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
