from django.db import models


class Incident(models.Model):
    msg = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=False, blank=False)
    source = models.CharField(max_length=255, null=False, blank=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}: {self.msg}, status: {self.status}, source: {self.source}, time: {self.time}"