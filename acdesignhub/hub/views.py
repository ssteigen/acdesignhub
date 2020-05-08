from django.shortcuts import render
from django.http import HttpResponseRedirect


import django_tables2 as tables

from .models import Design
from .tables import DesignTable
from .forms import DesignForm


class TableView(tables.SingleTableView):
    """A django-tables2 view for listing the approved designs."""
    table_class = DesignTable
    queryset = Design.objects.approved()
    template_name = 'hub/index.html'


def new(request):
    if request.method == 'POST':
        form = DesignForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            raise RuntimeError(form.errors)
    else:
        """A view for uploading a new design."""
        form = DesignForm()
        return render(request, 'hub/new.html', {
            'form': form
        })
