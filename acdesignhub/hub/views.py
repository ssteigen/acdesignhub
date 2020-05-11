from django.shortcuts import render
from django.http import HttpResponseRedirect


import django_tables2 as tables

from .models import Design
from .tables import DesignTable
from .forms import DesignForm

def index(request):
    designs = Design.objects.approved()
    design_types = Design.TYPE_CHOICES

    if "design_type" in request.GET:
        designs = designs.filter(design_type=request.GET['design_type'])

    return render(request, 'hub/index.html', {
        'designs': designs,
        'design_types': design_types,
        'design_type_selected': request.GET.get('design_type'),
    })

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
