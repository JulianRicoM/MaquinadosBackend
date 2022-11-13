from django.db import models
from django.utils.translation import gettext as _

from Applications.client.models import BaseModel
from Applications.employee.models import Employee


# --------------------------------- STATUS TOOLS --------------------------------
class StatusTools(models.Model):
    status = models.CharField(verbose_name = _('Status Tools'), max_length = 15)
    
    def __str__(self):
        return self.status

# --------------------------------- TOOLS --------------------------------
class Tools(BaseModel):
    employee_id = models.ForeignKey(Employee, on_delete = models.CASCADE, verbose_name = _('Employee'))
    trademark = models.CharField(verbose_name = _('Trademark'), max_length = 20)
    dimension = models.CharField(verbose_name = _('Dimension'), max_length = 20)
    status_tool = models.ForeignKey(StatusTools, on_delete = models.CASCADE, verbose_name = _('Status Tool'))
