# https://stackoverflow.com/questions/23766312/django-fields-default-value-from-model-instance

from django.contrib.auth.models import AbstractUser
from django.db import models

def create_folder_name(first_name, last_name):
    return first_name + last_name

class User(AbstractUser):
    folder_name = models.CharField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        if not self.folder_name:
            self.folder_name = create_folder_name(self.first_name, self.last_name)
        super(User, self).save(*args, **kwargs)

    # def save(self, *args, **kwargs):
        # self.folder_name = create_folder_name(self.first_name, self.last_name)
        # super(User, self).save(*args, **kwargs)
