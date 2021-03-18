from django.contrib import admin
from indent.models import IndentMaster, IndentTransactions

class IndentMasterAdmin(admin.ModelAdmin):
    list_display = ['id', 'indented_by', 'indent_date',]
    list_filter = ['id', 'indent_date']
    search_fields = ['id', 'indented_by']


class IndentTransactionsAdmin(admin.ModelAdmin):
    list_display = ['indent_master', 'part', 'indent_quantity','last_updated']
    list_filter = ['indent_master', 'part']
    search_fields = ['indent_master', 'part']

admin.site.register(IndentMaster, IndentMasterAdmin)
admin.site.register(IndentTransactions,IndentTransactionsAdmin)