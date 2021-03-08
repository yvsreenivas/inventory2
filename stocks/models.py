from django.db import models
from django.contrib.auth.models import User

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

class UserProfileInfo(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	portfolio_site = models.URLField(blank=True)
	profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
	def __str__(self):
	  return self.user.username

class SubCategory(models.Model):
	name = models.CharField(max_length=50, blank=False, null=False, help_text='Enter Sub-Category')
	def __str__(self):
		return self.name


class Stock(models.Model):
	category = models.CharField(max_length=15,blank=False,null=False,
					choices=category_choice, help_text='Select Item Category')
	subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE,help_text='Select Sub Category')
	part_no = models.CharField(max_length=15, blank=False, null=False, unique=True, 
                verbose="Part No",help_text='Enter 13 digit Part No')
	item_no = models.CharField(max_length=25, blank=True, null=True, verbose="Item/Asset No", help_text='Enter Asset No')
	HSN_code = models.CharField(max_length=10, blank=True, null=True, verbose="HSN No")
	item_name = models.CharField(max_length=50, blank=True, null=True,verbose="Item No"help_text='Enter Item Name')
	manufacturer = models.CharField(max_length=50, blank=True, null=True,verbose="Manufacturer")
	quantity = models.IntegerField(default='0', blank=True, null=True, verbose="Quantity in stock")
	units = models.CharField(max_length=5,blank=False,null=False,
					choices=units_choice, verbose="Units of Measurement")
	rate = models.DecimalField(decimal_places=2,max_digits=12,default=0, verbose="Rate")
	receive_quantity = models.IntegerField(default='0', blank=True, null=True, )
	receive_rate = models.DecimalField(decimal_places=2,max_digits=12,default=0)
	receive_by = models.CharField(max_length=50, blank=True, null=True)
	issue_quantity = models.IntegerField(default='0', blank=True, null=True)
	issue_by = models.CharField(max_length=50, blank=True, null=True)
	issue_to = models.CharField(max_length=50, blank=True, null=True)
	created_by = models.CharField(max_length=50, blank=True, null=True)
	reorder_level = models.IntegerField(default='0', blank=True, null=True, verbose="Reorder Level")
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_by = models.CharField(max_length=50, blank=False, null=False)

	def __str__(self):
		return self.item_name

class Issues(models.Model):
	stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
	issue_quantity = models.DecimalField(default='0', max_digits=10, decimal_places=2, blank=True, null=True)
	units = models.CharField(max_length=5,blank=False,null=False,
					choices=units_choice)
	issue_to = models.ForeignKey(User,on_delete=models.CASCADE)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_by = models.CharField(max_length=50, blank=False, null=False)

	def __str__(self):
		return self.stock.item_name

class Indent (models.Model):
	indented_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='indentor')
	part_no = models.ForeignKey(Stock, on_delete=models.CASCADE)
	indent_quantity = models.DecimalField(max_digits=10,decimal_places=2,default='0', blank=True, null=True)
	units = models.CharField(max_length=5,blank=False,null=False,
					choices=units_choice)
	required_for = models.CharField(max_length=50, blank=True, null=True)
	remarks = models.CharField(max_length=50, blank=True, null=True)
	approved = models.BooleanField(default=False, null=True)
	indent_approved_by = models.ForeignKey(User, on_delete=models.CASCADE)
	approved_on = models.DateTimeField(auto_now_add=False, auto_now=True)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self):
		return self.stock.item_name

# Create your models here.
