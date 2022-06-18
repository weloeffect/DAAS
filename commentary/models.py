from django.db import models

# Create your models here.
class Commentary(models.Model):
    first_name = models.CharField(max_length= 20)
    last_name = models.CharField(max_length= 20)
    email = models.EmailField(max_length=20)
    comment = models.TextField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name