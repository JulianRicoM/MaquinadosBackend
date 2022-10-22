
from django.db import models
from django.utils.translation import gettext as _


# --------------------------------- BASEMODEL ---------------------------------
class BaseModel(models.Model):
    
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# --------------------------------- COUNTRY ---------------------------------
class Country(models.Model):
    country = models.CharField(verbose_name = _('Country'), max_length = 50)
    
    def __str__(self):
        return self.country

# --------------------------------- DEPARTMENT ---------------------------------
class Department(models.Model):
    department = models.CharField( verbose_name= _('Department'), max_length = 50)
    country = models.ForeignKey(Country, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.department

# --------------------------------- CITY ---------------------------------    
class City(models.Model):
    city =  models.CharField(verbose_name = _('City'), max_length = 50)
    department = models.ForeignKey(Department, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.city

# --------------------------------- PERSON --------------------------------
class Person(BaseModel):
    name = models.CharField(verbose_name = _("Name"), max_length = 30)
    phone_number = models.CharField(verbose_name = _("Phone Number"), max_length = 12)
    email = models.EmailField(verbose_name = _('Email'), max_length = 40)
    address = models.CharField(verbose_name = _('Address'), max_length = 20)
    
# --------------------------------- CLIENT --------------------------------
class Client(Person):
    nit = models.CharField(verbose_name = _("Nit"), max_length = 30, primary_key = True)
    country = models.ForeignKey(Country, on_delete = models.CASCADE)
    departament = models.ForeignKey(Department, on_delete = models.CASCADE)
    city = models.ForeignKey(City, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
    