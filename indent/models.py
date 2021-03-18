from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from stocks.models import PartsMaster

category_choice = (
        ('Asset', 'Asset'),
        ('Consumables', 'Consumables'),
    )

units_choice = (
            ('Kgs', 'Kgs'),
            ('gms', 'Gms'),
            ('Nos', 'Nos'),
            ('Ltrs', 'Ltrs'),
            ('Mtrs', 'Mtrs')
    )


# Create your models here.
class IndentMaster (models.Model):
    indented_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='indents',)
    indent_date = models.DateField(auto_now_add=False, auto_now=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    note = models.TextField(blank=True)

    # def __str__(self):
    #     return str(self.indent_no)

    # class Meta:
    #     ordering = ['id']


class IndentTransactions (models.Model):
    """ 
    A class for creating indents for multiple parts
    
    """
    indent_master = models.ForeignKey(IndentMaster, on_delete=models.CASCADE,
                                    related_name='has_indents',
                                    verbose_name="Indent No")
    part = models.ForeignKey(PartsMaster, on_delete=models.CASCADE, related_name='indented_part')
    indent_quantity = models.DecimalField(max_digits=10, decimal_places=2,
                                          default='0',
                                          blank=True, null=True,
                                          verbose_name='Indented Quantity')
    units = models.CharField(max_length=5, blank=False, null=False,
                             choices=units_choice, verbose_name="Units")
    required_for = models.CharField(max_length=50, blank=True,
                                    null=True, verbose_name="Required for")
    approved = models.BooleanField(default=False, null=True,
                                   verbose_name="Approved?")
    #indent_approved_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    approved_on = models.DateTimeField(auto_now_add=False, auto_now=True,
                                       verbose_name="Approved on")
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    # def __str__(self):
    #     return self.part.item_name

    # class Meta:
    #     ordering = ['part']
