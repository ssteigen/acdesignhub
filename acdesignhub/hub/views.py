from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.db.models import F

import django_tables2 as tables

from .models import Design
from .tables import DesignTable
from .forms import DesignForm

def index(request):
    designs = Design.objects.approved()
    design_types = Design.TYPE_CHOICES

    requested_types = request.GET.getlist('design_type')
    requested_types = map(str.capitalize, requested_types)
    requested_types = [sub.replace('_', ' ') for sub in requested_types]

    if "design_type" in request.GET:
        designs = designs.filter(design_type__in=request.GET.getlist('design_type'))

    if "creator_code" in request.GET:
        designs = designs.filter(creator_code=request.GET['creator_code'])

    return render(request, 'hub/index.html', {
        'designs': designs,
        'design_types': design_types,
        'design_type_selected': requested_types,
    })

def detail(request, design_code):
    design = Design.objects.approved().get(design_code=design_code)
    related_designs = Design.objects.approved().filter(creator_code=design.creator_code).exclude(pk=design.pk)

    # increment view counter
    design.view_count += 1
    design.save()

    return render(request, 'hub/design.html', {
        'design': design,
        'related_designs': related_designs
    })

def download(request, design_code):
    design = Design.objects.approved().get(design_code=design_code)

    # increment view counter
    design.download_count += 1
    design.save()

    filename = design.original_image.name

    response = HttpResponse(design.original_image.open(), content_type='application/force-download')
    response['Content-Disposition'] = f"attachment; filename={filename}"

    return response


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
