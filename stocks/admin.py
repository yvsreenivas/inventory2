from django.contrib import admin
from .forms import PartsMasterCreateForm
from .models import SubCategory, PartsMaster, Indent, Issues


class PartsCreateFormAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'subcategory', 'part_no', 'item_name',
                    'quantity']
    form = PartsMasterCreateForm
    list_filter = ['category', 'subcategory']
    search_fields = ['category', 'item_name']


class IssuesAdmin(admin.ModelAdmin):
    list_display = ['stock', 'issue_quantity', 'issue_to', 'updated_by',
                    'last_updated']


admin.site.register(SubCategory)
admin.site.register(PartsMaster, PartsCreateFormAdmin)
admin.site.register(Issues)
admin.site.register(Indent)
