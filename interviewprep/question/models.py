from django.db import models

# Create your models here.


class Questions(models.Model):
    q = models.CharField(max_length=255)

    def __str__(self):
        return self.q

