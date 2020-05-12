from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.db.models import F

import django_tables2 as tables

from .models import Design
from .tables import DesignTable
from .forms import DesignForm

def index(request):
    designs = Design.objects.approved()
    design_types = Design.TYPE_CHOICES

    if "design_type" in request.GET:
        designs = designs.filter(design_type=request.GET['design_type'])

    if "creator_code" in request.GET:
        designs = designs.filter(creator_code=request.GET['creator_code'])

    if "design_code" in request.GET:
        designs = designs.filter(design_code=request.GET['design_code'])
        # if there is more than one design, throw an error.
        design = designs[0]
        related_designs = Design.objects.approved().filter(creator_code=design.creator_code).exclude(design_code=design.design_code)

        # increment view counter
        Design.objects.filter(design_code=request.GET['design_code']).update(view_count=F('view_count')+1)

        return render(request, 'hub/design.html', {
            'design': design,
            'related_designs': related_designs
        })

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
