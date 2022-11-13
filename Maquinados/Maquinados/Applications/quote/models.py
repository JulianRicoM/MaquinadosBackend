from django.db import models
from django.utils.translation import gettext as _

from Applications.client.models import BaseModel, Client
from Applications.employee.models import Employee
from Applications.item.models import Item

# --------------------------------- STATUS QUOTE --------------------------------
class StatusQuote(models.Model):
    status_description = models.CharField(verbose_name = _('Status Description'), max_length = 30)

    def __str__(self):
        return self.status_description
    
# --------------------------------- QUOTE --------------------------------
class Quote(BaseModel):
    quote_number = models.CharField(verbose_name = _('Quote Number'), max_length = 30)
    client_id = models.ForeignKey(Client, on_delete = models.CASCADE, verbose_name = 'Client', max_length = 30)
    document_employee = models.ForeignKey(Employee, on_delete = models.CASCADE, verbose_name = _('Employee Document'), max_length = 20)
    item_id = models.ForeignKey(Item, verbose_name=_("Item Id"), on_delete=models.CASCADE, max_length = 10)
    quantity = models.IntegerField(verbose_name = _('Quantity'))
    total_amount = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = _('Total Amount'))
    expitation_date = models.DateField(verbose_name = _('Expiration Date'))
    status_id = models.ForeignKey(StatusQuote, on_delete = models.CASCADE, verbose_name = _('Status'))
    
    def __str__(self):
        return self.quote_number
    
