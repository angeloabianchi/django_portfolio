from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='jobs/images/')
    summary = models.CharField(max_length=255)

    def __str__(self):
        return self.name