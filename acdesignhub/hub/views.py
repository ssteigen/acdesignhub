from django.contrib import messages
from django.forms import modelformset_factory
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.db.models import Count

from .models import Design, Image
from .forms import DesignForm, ImageForm

def index(request):
    designs = Design.objects.approved().annotate(number_of_images=Count('image'))
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

    additional_images = design.image_set.all()

    # increment view counter
    design.view_count += 1
    design.save()

    return render(request, 'hub/design.html', {
        'design': design,
        'additional_images': additional_images,
        'related_designs': related_designs,
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
    ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=3)

    if request.method == 'POST':
        form = DesignForm(request.POST, request.FILES)
        formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())

        if form.is_valid() and formset.is_valid():
            design = form.save()

            imageset_forms = filter(bool, formset.cleaned_data)
            for imageset in imageset_forms:
                print(imageset)
                image = imageset['image']
                photo = Image(design=design, image=image)
                photo.save()

            messages.success(request, 'Posted!')
            return HttpResponseRedirect('/')
        else:
            raise RuntimeError(form.errors)
    else:
        """A view for uploading a new design."""
        form = DesignForm()
        formset = ImageFormSet(queryset=Image.objects.none())
        return render(request, 'hub/new.html', {
            'form': form,
            'formset': formset
        })
