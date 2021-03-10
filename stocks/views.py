from django.shortcuts import render, redirect
from django.contrib import messages
from .models import PartsMaster, SubCategory, Issues
from .forms import PartsMasterCreateForm, PartsMasterSearchForm
from .forms import PartsMasterUpdateForm, IssueForm, ReceiveForm, \
     IssueCreateForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import csv
from django.db.models import Sum, F, FloatField
from django.views import generic


@login_required
def list_items(request):
    title = 'List of Assets and Consumables'
    form = PartsMasterSearchForm(request.POST or None)
    queryset = PartsMaster.objects.all()
    total = (PartsMaster.objects
             .aggregate(total=Sum(F('rate') * F('quantity'),
                        output_field=FloatField()))['total'])
    context = {
        "header": title,
        "queryset": queryset,
        "total": total,
        "form": form,
    }
    if request.method == 'POST':
        queryset = PartsMaster.objects.filter(
                   item_name__icontains=form['item_name'].value(),
                   category__icontains=form['category'].value(),
        )
        total = queryset.aggregate(total=Sum(F('rate') *
                                             F('quantity'),
                                   output_field=FloatField()))['total']

        if form['export_to_CSV'].value() is True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=\
                     "List of stock.csv"'
            writer = csv.writer(response)
            writer.writerow(['CATEGORY', 'SUB CATEGORY', 'PART NO',
                             'ITEM NO', 'ITEM NAME', 'QUANTITY', 'UNITS',
                             'RATE', 'VALUE'])
            instance = queryset
            for stock in instance:
                writer.writerow([stock.category, stock.subcategory,
                                 stock.part_no, stock.item_no, stock.item_name,
                                 stock.quantity, stock.units, stock.rate,
                                 (stock.quantity * stock.rate)])
            return response

        context = {
            "form": form,
            "header": title,
            "total": total,
            "queryset": queryset,
        }
    return render(request, "stocks/list_items.html", context)


@login_required
def add_items(request):
    form = PartsMasterCreateForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.updated_by = request.user.username
        instance.save()

        messages.success(request, 'Successfully Saved')
        return redirect('add_items')
    context = {
        "form": form,
        "header": "Add Assets or Consumables",
    }
    return render(request, "stocks/add_items.html", context)


@login_required
def update_items(request, pk):
    queryset = PartsMaster.objects.get(id=pk)
    form = PartsMasterUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = PartsMasterUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Saved')
            return redirect('list_items')

    context = {
        'form': form,
        "header": "Update Assets or Consumables",
    }
    return render(request, 'stocks/update_items.html', context)


@login_required
def delete_items(request, pk):
    queryset = PartsMaster.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Successfully Deleted')
        return redirect('list_items')
    return render(request, 'stocks/delete_items.html')


@login_required
def stock_detail(request, pk):
    queryset = PartsMaster.objects.get(id=pk)
    context = {
        "queryset": queryset,
    }
    return render(request, "stocks/stock_detail.html", context)


@login_required
def issue_items(request, pk):
    queryset = PartsMaster.objects.get(id=pk)
    form = IssueForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.quantity -= instance.issue_quantity
        # instance.issue_by = str(request.user)
        messages.success(request, "Issued SUCCESSFULLY. "
                         + str(instance.quantity) + " "
                         + str(instance.item_name) + "s now left in Store")
        instance.save()

        return redirect('/stock_detail/'+str(instance.id))
        # return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": 'Issue ' + str(queryset.item_name),
        "queryset": queryset,
        "form": form,
        "username": 'Issue By: ' + str(request.user),
    }
    return render(request, "stocks/add_items.html", context)


@login_required
def receive_items(request, pk):
    queryset = PartsMaster.objects.get(id=pk)
    form = ReceiveForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.quantity += instance.receive_quantity
        instance.save()
        messages.success(request, "Received SUCCESSFULLY. "
                         + str(instance.quantity) + " "
                         + str(instance.item_name)+"s now in Store")

        return redirect('/stocks/stock_detail/'+str(instance.id))
        # return HttpResponseRedirect(instance.get_absolute_url())
    context = {
            "title": 'Receive ' + str(queryset.item_name),
            "instance": queryset,
            "form": form,
            "username": 'Receive By: ' + str(request.user),
        }
    return render(request, "stocks/add_items.html", context)


@login_required
def issue_items2(request, pk):
    a = PartsMaster.objects.get(id=pk)
    if request.method == 'POST':
        f = IssueCreateForm(request.POST)
        if f.is_valid():
            instance = f.save(commit=False)
            instance.updated_by = request.user.username
            if a.quantity >= instance.issue_quantity:
                a.quantity -= instance.issue_quantity
                a.save()
                instance.part = a
                messages.success(request, "Issued SUCCESSFULLY. "
                                 + str(a.quantity) + " "
                                 + str(a.item_name)
                                 + "s now left in Store")
                instance.save()
            else:
                messages.error(request, "Issued failed. " + str(a.quantity)
                               + " " + str(a.item_name)
                               + "s is not enough to complete the issue")

            return redirect('/stocks/stock_detail/'+str(a.id))
    f = IssueCreateForm(request.POST)
    context = {
        "title": 'Issue ' + str(a.item_name),
        "queryset": a,
        "form": f,
        "username": 'Issue By: ' + str(request.user),
    }
    return render(request, "stocks/add_items.html", context)


class PartsMasterListView(generic.ListView):
    model = PartsMaster
    paginate_by = 10


class PartsMasterDetailView(generic.DetailView):
    model = PartsMaster
