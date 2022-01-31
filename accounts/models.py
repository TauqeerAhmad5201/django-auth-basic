# Create your models here.
from pickle import NONE
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    firstname = models.CharField(_('firstname'),max_length=100,default='DEFAULT VALUE')
    email = models.EmailField(_('email address'), unique=True)
    height = models.IntegerField(_('height'), name='height', default=0 )

    USERNAME_FIELD = 'email'                               #login field 
    REQUIRED_FIELDS = ['firstname','height']

    objects = CustomUserManager()

    def __str__(self):
        return self.email