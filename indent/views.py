from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from indent.models import *
from indent.forms import IndentTransactionsFormset, IndentMasterForm
from django.db import transaction
from django.http import HttpResponse



##########################################################################
#                           Indent views                             #
##########################################################################

class HomepageView(TemplateView):
    template_name = "indent/base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['indents'] = IndentMaster.objects.order_by('id')
        return context


class IndentMasterDetailView(DetailView):
    model = IndentMaster
    template_name = 'indent/indentmaster_detail.html'

    def get_context_data(self, **kwargs):
        context = super(IndentMasterDetailView, self).get_context_data(**kwargs)
        return context


class IndentMasterCreate(CreateView):
    model = IndentMaster
    template_name = 'indent/indentmaster_create.html'
    form_class = IndentMasterForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(IndentMasterCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['indents'] = IndentTransactionsFormset(self.request.POST)
        else:
            print("*********")
            data['indents'] = IndentTransactionsFormset()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        indents = context['indents']
        with transaction.atomic():
            print("*******************************")
            form.instance.indented_by = self.request.user
            self.object = form.save()
            if indents.is_valid():
                indents.instance = self.object
                indents.save()
        return super(IndentMasterCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('school_indents:indentmaster_detail', kwargs={'id': self.object.id})
