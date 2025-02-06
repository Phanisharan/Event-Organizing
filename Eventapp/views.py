from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import ContactForm

def home(request):
    card_data = Card.objects.all().order_by('-id')
    gallery_data1 = Gallery.objects.all().order_by('-id')
    gallery_data2 = Gallery.objects.all()

    return render(request, 'Home.html', {'card_data': card_data, 'gallery_data': gallery_data1, 'gallery_data2' : gallery_data2})

def planningservices(request):
    service_data = Services.objects.all()
    return render(request, 'PlanningServices.html', {'service_data': service_data})

def viewdetail(request, id):
    data = Services.objects.get(id=id)
    venue = Venue.objects.all()
    ocassion = Ocassion.objects.all()
    decoration = Decoration.objects.all()
    photography = Photography.objects.all()
    return render(request, f'details/Viewdetail{id}.html', {
        'data': data,
        'venue': venue,
        'ocassion': ocassion,
        'decoration': decoration,
        'photography': photography
    })

def gallery(request):
    gallery_data = Gallery.objects.all().order_by('-id')
    return render(request, 'Gallery.html', {'gallery_data': gallery_data})

def venue(request):
    packages = Packages.objects.all().order_by('-id')[:3]
    card_data = Card.objects.all().order_by('-id')
    couple_moments = CoupleMoments.objects.all()
    return render(request, 'Venue.html', {
        'packages': packages,
        'card_data': card_data,
        'couple_moments': couple_moments
    })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Eventapp:thankyou')
        else:
            print("Form is not valid")
    else:
        print("Received GET request")
    
    s1 = ContactForm()
    return render(request, 'Contact.html', {'form': s1})

def thankyou(request):
    return render(request, 'Thankyou.html')

def wedding_gallery(request, id):
    couple_moment = get_object_or_404(CoupleMoments, id=id)
    galleries = WeddingGallery.objects.filter(names=couple_moment)
    print(f"Couple Moment: {couple_moment.names}, Galleries Count: {galleries.count()}")
    
    for gallery in galleries:
        print(f"Gallery: {gallery.description}, Image: {gallery.images}")
    
    return render(request, 'details2/Viewdetail.html', {
        'wedding_data': galleries,
        'couple_moment': couple_moment
    })