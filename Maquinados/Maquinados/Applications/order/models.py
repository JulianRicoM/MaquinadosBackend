from django.db import models
from django.utils.translation import gettext as _

from Applications.client.models import BaseModel
from Applications.employee.models import Employee
from Applications.quote.models import Quote

# --------------------------------- ORDER PROCESS -------------------------------- 
# Process in which the order is
class OrderProcess(models.Model):
    order_process = models.CharField(verbose_name = _('Order Status'), max_length = 20)
    
    def __str__(self):
        return self.order_process

# --------------------------------- ORDER STATUS--------------------------------
# Order was paid or not 
class OrderStatus(models.Model):
    order_status = models.CharField(verbose_name = _('Order Status'), max_length = 20)
    
    def __str__(self):
        return self.order_status

# --------------------------------- CURRENCY --------------------------------
class Currency(models.Model):
    currency_name = models.CharField(verbose_name = _('Currency'), max_length = 20)
    
    def __str__(self):
        return self.currency_name
    

# --------------------------------- PAYMENT METHOD --------------------------------
class PaymentMethod(models.Model):
    payment_name = models.CharField(verbose_name = _('Payment'), max_length = 20)

    def __str__(self):
        return self.payment_name
# --------------------------------- ORDER --------------------------------
class Order(BaseModel):
    quote_number = models.ForeignKey(Quote, on_delete  = models.CASCADE, verbose_name = _('Quote Number'))
    emloyee_id = models.ForeignKey(Employee, verbose_name=_("Employee"), on_delete = models.CASCADE)
    payment_method = models.ForeignKey(PaymentMethod, on_delete = models.CASCADE, verbose_name = _('Payment Method'))
    discount = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = _('Discount'))
    subtotal = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = _('Subtotal'))
    sure = models.CharField(verbose_name = _('Sure Name'), max_length = 25)
    freigth = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = _('Freigth'))
    various_expenses = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = _('Various Expenses'))
    amount_whitout_vat = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = _('Amount Whitout VAT'))
    total_amount = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = _('Total Amount'))
    currency = models.ForeignKey(Currency, on_delete = models.CASCADE, verbose_name = _('Currency'))
    delivery_address = models.CharField(verbose_name = _('Delivery Address'), max_length = 40)
    status_id = models.ForeignKey(OrderStatus, on_delete = models.CASCADE, verbose_name = _('Status'))
    process_id = models.ForeignKey(OrderProcess, on_delete = models.CASCADE, verbose_name = _('Process'))
    