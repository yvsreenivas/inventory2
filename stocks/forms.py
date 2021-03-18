from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from stocks.models import PartsMaster, Issues
# from django.contrib.auth.models import User


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

class PMCreateForm(forms.ModelForm):
    class Meta:
        model = PartsMaster
        fields = ['category', 'subcategory', 'part_no', 'item_no']
        widgets = {'part_no': forms.TextInput(attrs={'data-mask':
                                                     "000-00-00000-00"})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('category', css_class='form-group col-md-6 mb-0'),
                Column('subcategory', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('part_no', css_class='form-group col-md-6 mb-0'),
                Column('item_no', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
        )


class PartsMasterCreateForm(forms.ModelForm):
    class Meta:
        model = PartsMaster
        fields = ['category', 'subcategory', 'part_no', 'item_no',
                  'item_name', 'manufacturer', 'quantity', 'units', 'rate',
                  'reorder_level']
        # labels = {  'category': ('Category of the item'),}
        widgets = {'part_no': forms.TextInput(attrs={'data-mask':
                                                     "000-00-00000-00"})}

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category:
            raise forms.ValidationError('This field is required')
        return category

    def clean_sub_category(self):
        subcategory = self.cleaned_data.get('subcategory')
        if not subcategory:
            raise forms.ValidationError('This field is required')
        return subcategory

    def clean_part_no(self):
        part_no = self.cleaned_data.get('part_no')
        if not part_no:
            raise forms.ValidationError('This field is required')

        Parts = PartsMaster.objects.all()
        for instance in Parts:
            if instance.part_no == part_no:
                raise forms.ValidationError(part_no + " exists")
        return part_no

    def clean_item_no(self):
        item_no = self.cleaned_data.get('item_no')

        return item_no

    def clean_units(self):
        units = self.cleaned_data.get('units')
        if not units:
            raise forms.ValidationError('This field is required')
        return units

    def clean_item_name(self):
        item_name = self.cleaned_data.get('item_name')
        if not item_name:
            raise forms.ValidationError('This field is required')

        Parts = PartsMaster.objects.all()
        for instance in Parts:
            if instance.item_name == item_name:
                raise forms.ValidationError(item_name + " exists")
        return item_name

    def clean_manufacturer(self):
        manufacturer = self.cleaned_data.get('manufacturer')
        if not manufacturer:
            raise forms.ValidationError('This field is required')
        return manufacturer


class PartsMasterSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)

    class Meta:
        model = PartsMaster
        fields = ['item_name', 'category', ]


class PartsMasterUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['subcategory'].widget.attrs['disable'] = True

    class Meta:
        model = PartsMaster
        fields = ['category', 'subcategory', 'part_no', 'item_no',
                  'item_name', 'manufacturer', 'quantity', 'units', 'rate']

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category:
            raise forms.ValidationError('This field is required')
        return category

    def clean_sub_category(self):
        subcategory = self.cleaned_data.get('subcategory')
        if not subcategory:
            raise forms.ValidationError('This field is required')
        return subcategory

    def clean_part_no(self):
        part_no = self.cleaned_data.get('part_no')
        if not part_no:
            raise forms.ValidationError('This field is required')
        return part_no

    def clean_item_no(self):
        item_no = self.cleaned_data.get('item_no')

        return item_no

    # def clean_HSN_code(self):
    #   HSN_code = self.cleaned_data.get('HSN_code')
    #   if not HSN_code:
    #     raise forms.ValidationError('This field is required')
    #   return HSN_code

    def clean_units(self):
        units = self.cleaned_data.get('units')
        if not units:
            raise forms.ValidationError('This field is required')
        return units

    def clean_item_name(self):
        item_name = self.cleaned_data.get('item_name')
        if not item_name:
            raise forms.ValidationError('This field is required')
        return item_name

    def clean_manufacturer(self):
        manufacturer = self.cleaned_data.get('manufacturer')
        if not manufacturer:
            raise forms.ValidationError('This field is required')
        return manufacturer


class IssueForm(forms.ModelForm):

    class Meta:
        model = PartsMaster
        fields = ['issue_quantity', 'issue_to']


class ReceiveForm(forms.ModelForm):

    class Meta:
        model = PartsMaster
        fields = ['receive_quantity']


class IssueCreateForm(forms.ModelForm):

    class Meta:
        model = Issues
        fields = ['issue_quantity',  'issue_to']

    def clean_issue_quantity(self):
        issue_quantity = self.cleaned_data.get('issue_quantity')
        if not issue_quantity:
            raise forms.ValidationError('This field is required')
        return issue_quantity

    def clean_issue_to(self):
        issue_to = self.cleaned_data.get('issue_to')
        if not issue_to:
            raise forms.ValidationError('This field is required')
        return issue_to
