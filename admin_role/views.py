from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import *
from Eventapp.forms import ContactForm
from Eventapp.models import *


@login_required
def custom_admin(request):
    if request.method == 'POST':
        if 'card_submit' in request.POST:
            form = CardForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        elif 'gallery_submit' in request.POST:
            form = GalleryForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        elif 'services_submit' in request.POST:
            form = ServicesForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        elif 'packages_submit' in request.POST:
            form = PackagesForm(request.POST)
            if form.is_valid():
                form.save()
        elif 'weddinggallery_submit' in request.POST:
            form = WeddingGalleryForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        elif 'couplemoments_submit' in request.POST:
            form = CoupleMomentsForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        elif 'venue_submit' in request.POST:
            form = VenueForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        elif 'ocassion_submit' in request.POST:
            form = OcassionForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        elif 'decoration_submit' in request.POST:
            form = DecorationForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        elif 'photography_submit' in request.POST:
            form = PhotographyForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        return redirect('Eventapp:custom_admin')

    context = {
        'card_form': CardForm(),
        'gallery_form': GalleryForm(),
        'services_form': ServicesForm(),
        'packages_form': PackagesForm(),
        'couplemoments_form': CoupleMomentsForm(),
        'weddinggallery_form': WeddingGalleryForm(),
        'venue_form': VenueForm(),
        'ocassion_form': OcassionForm(),
        'decoration_form': DecorationForm(),
        'photography_form': PhotographyForm(),
    }
    return render(request, 'admin/AdminPage.html', context)


@login_required
def records_page(request):
    cards = Card.objects.all()
    galleries = Gallery.objects.all()
    services = Services.objects.all()
    packages = Packages.objects.all()
    couplemoments = CoupleMoments.objects.all()
    weddinggalleries = WeddingGallery.objects.all()
    venues = Venue.objects.all()
    ocassions = Ocassion.objects.all()
    decorations = Decoration.objects.all()
    photographys = Photography.objects.all()

    context = {
        'cards': cards,
        'galleries': galleries,
        'services': services,
        'packages': packages,
        'couplemoments': couplemoments,
        'weddinggalleries': weddinggalleries,
        'venues': venues,
        'ocassions': ocassions,
        'decorations': decorations,
        'photographys': photographys
    }
    return render(request, 'admin/RecordsPage.html', context)



@login_required
def edit_record(request, model, id):
    model_class = {
        'card': Card,
        'gallery': Gallery,
        'services': Services,
        'packages': Packages,
        'couplemoments': CoupleMoments,
        'weddinggallery': WeddingGallery,
        'venue': Venue,
        'ocassion': Ocassion,
        'decoration': Decoration,
        'photography': Photography
    }[model]

    form_class = {
        'card': CardForm,
        'gallery': GalleryForm,
        'services': ServicesForm,
        'packages': PackagesForm,
        'couplemoments': CoupleMomentsForm,
        'weddinggallery': WeddingGalleryForm,
        'venue': VenueForm,
        'ocassion': OcassionForm,
        'decoration': DecorationForm,
        'photography': PhotographyForm,
    }[model]

    record = get_object_or_404(model_class, id=id)
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=record)
        if form.is_valid():
            form.save()
            return redirect('Eventapp:records_page')
    else:
        form = form_class(instance=record)

    return render(request, 'admin/EditRecord.html', {'form': form, 'model': model, 'id': id})


@login_required
def delete_record(request, model, id):
    model_class = {
        'card': Card ,
        'gallery': Gallery,
        'services': Services,
        'packages': Packages,
        'couplemoments': CoupleMoments,
        'weddinggallery': WeddingGallery,
        'venue': Venue,
        'ocassion': Ocassion,
        'decoration': Decoration,
        'photography': Photography,
        'contacts': Contact,
    }[model]

    record = get_object_or_404(model_class, id=id)
    if request.method == 'POST':
        record.delete()
        return redirect('Eventapp:records_page')
    return render(request, 'admin/DeleteRecord.html', {'model': model, 'id': id})


@login_required
def tracked_info(request):
    contact_entries = Contact.objects.all()
    context = {
        'contact_entries': contact_entries,
    }
    return render(request, 'admin/TrackedInfo.html', context)



def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Eventapp:login')
    else:
        form = RegisterForm()
    return render(request, 'admin/Register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Eventapp:custom_admin')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'admin/Login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('Eventapp:login')