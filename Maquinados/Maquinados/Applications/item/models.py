from django.db import models
from django.utils.translation import gettext as _

from Applications.client.models import  BaseModel

# --------------------------------- MATERIAL ---------------------------------
class Material(models.Model):
    description = models.CharField( max_length = 50 )
    
    def __str__(self):
        return self.description
# --------------------------------- MEASUREMENT UNITS ---------------------------------
class Measurement_units(models.Model):
    description = models.CharField( max_length = 50 )
    
    def __str__(self):
        return self.description    
    
# --------------------------------- ITEM ---------------------------------
class Item(BaseModel):
    name = models.CharField(verbose_name = _('Name'), max_length = 30)
    reference = models.CharField(verbose_name = ('Reference'), max_length = 30)
    plane = models.FileField( upload_to = 'media')
    surface_finish = models.CharField( verbose_name = _('Surface Finish'), max_length = 15)
    material_id = models.ForeignKey(Material, verbose_name =_("Material Type"), on_delete = models.CASCADE)
    tolerance = models.IntegerField(blank = True, null = True, verbose_name = _('Tolerance'))
    linear = models.IntegerField(blank = True, null = True, verbose_name = _('Linear'))
    angular = models.IntegerField(blank = True, null = True, verbose_name = _('Angular'))
    size = models.IntegerField(verbose_name = _('Size'))
    volume = models.IntegerField(verbose_name = _('Volume'))
    measurement_units_id = models.ForeignKey(Measurement_units, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name
    