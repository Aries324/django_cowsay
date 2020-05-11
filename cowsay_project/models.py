from django.db import models


# Create your models here.
class UserTextInput(models.Model):
    text = models.CharField(max_length=80)

    def __str__(self):
        return self.text