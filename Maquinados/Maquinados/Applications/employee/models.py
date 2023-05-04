from django.db import models
from django.utils.translation import gettext as _
from django import forms

from Applications.client.models import Person

# --------------------------------- POSITION ---------------------------------
class Position(models.Model):
    position = models.CharField(verbose_name = _('Position'), max_length = 20)
    
    def __str__(self):
        return self.position


# --------------------------------- EPS ---------------------------------
class Eps(models.Model):
    eps_name = models.CharField(verbose_name = _('EPS'), max_length = 20)
    
    def __str__(self):
        return self.eps_name

# --------------------------------- EMPLOYEE ---------------------------------
class Employee(Person):
    document = models.CharField(unique = True, verbose_name = _('Document'), max_length = 20)
    last_name = models.CharField(verbose_name = _('Last Name'), max_length =20)
    position = models.ForeignKey(Position, on_delete = models.CASCADE, verbose_name = _('Position'))
    eps_id = models.ForeignKey(Eps, on_delete =  models.CASCADE, verbose_name = 'EPS')
    birthdate = models.DateField(widget=forms.PasswordInput, verbose_name = _('Password'))
    password = models.Pasw
    
    def __str__(self):
        return self.name
