from django.shortcuts import render
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
    """A view for uploading a new design."""
    form = DesignForm()

    return render(request, 'hub/new.html', {
        'form': form
    })
