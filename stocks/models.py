from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

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


class SubCategory(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False,
                            help_text='Enter Sub-Category')

    def __str__(self):
        return self.name


class PartsMaster(models.Model):
    category = models.CharField(max_length=15, blank=False, null=False,
                                choices=category_choice,
                                help_text='Select Item Category')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE,
                                    help_text='Select Sub Category')
    part_no = models.CharField(max_length=15, blank=False, null=False,
                               unique=True,
                               verbose_name="Part No",
                               help_text='Enter 13 digit Part No')
    item_no = models.CharField(max_length=25, blank=True, null=True,
                               verbose_name="Item/Asset No",
                               help_text='Enter Asset No')
    HSN_code = models.CharField(max_length=10, blank=True, null=True,
                                verbose_name="HSN No")
    item_name = models.CharField(max_length=50, blank=True, null=True,
                                 verbose_name="Item Name",
                                 help_text='Enter Item Name')
    manufacturer = models.CharField(max_length=50, blank=True, null=True,
                                    verbose_name="Manufacturer")
    quantity = models.IntegerField(default='0', blank=True, null=True,
                                   verbose_name="Quantity in PartsMaster")
    units = models.CharField(max_length=5, blank=False, null=False,
                             choices=units_choice,
                             verbose_name="Units of Measurement")
    rate = models.DecimalField(decimal_places=2, max_digits=12, default=0,
                               verbose_name="Rate")
    receive_quantity = models.IntegerField(default='0', blank=True,
                                           null=True,)
    receive_rate = models.DecimalField(decimal_places=2, max_digits=12,
                                       default=0)
    receive_by = models.CharField(max_length=50, blank=True, null=True)
    issue_quantity = models.IntegerField(default='0', blank=True, null=True)
    issue_by = models.CharField(max_length=50, blank=True, null=True)
    issue_to = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    reorder_level = models.IntegerField(default='0', blank=True, null=True,
                                        verbose_name="Reorder Level")
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_by = models.CharField(max_length=50, blank=False, null=False,
                                  verbose_name="Updated by")

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this partno."""
        return reverse('part-detail', args=[str(self.id)])

    class Meta:
        ordering = ['part_no', 'item_name']


class Issues(models.Model):
    part = models.ForeignKey(PartsMaster, on_delete=models.CASCADE)
    issue_quantity = models.DecimalField(default='0', max_digits=10,
                                         decimal_places=2,
                                         blank=True, null=True,
                                         verbose_name="Issue Quantity")
    units = models.CharField(max_length=5, blank=False, null=False,
                             choices=units_choice, verbose_name="Units")
    issue_to = models.ForeignKey(User, on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_by = models.CharField(max_length=50, blank=False, null=False,
                                  verbose_name="Updated by")

    def __str__(self):
        return self.part.item_name

    class Meta:
        ordering = ['part']


