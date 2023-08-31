from django.db import models
from loginregister.models import Userprofile
# Create your models here.


class Picture(models.Model):
    username = models.ForeignKey(Userprofile.user)
    picture = models.ImageField()