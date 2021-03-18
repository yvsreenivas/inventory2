from django import forms
from stocks.models import PartsMaster
from .models import IndentMaster, IndentTransactions
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from .custom_layout_object import *


class IndentTransactionsForm(forms.ModelForm):

    class Meta:
        model = IndentTransactions
        exclude = ()


IndentTransactionsFormset = inlineformset_factory(
        IndentMaster, IndentTransactions, form=IndentTransactionsForm,
        fields = ['part', 'indent_quantity', 'required_for'], extra=1, can_delete = True
    )


class IndentMasterForm(forms.ModelForm):

    class Meta:
        model = IndentMaster
        exclude = ['indented_by']

    def __init__(self, *args, **kwargs):
        super(IndentMasterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                #Field('indent_no'),
                # Field('indent_date'),
                Fieldset('Add indents',
                    Formset('indents')),
                Field('note'),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'save')),
                )
            )    