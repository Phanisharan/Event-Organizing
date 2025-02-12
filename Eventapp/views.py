from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
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
            contact_entry = form.save()  # Save form data to the database
            
            # Extract user details
            user_name = contact_entry.name
            user_surname = contact_entry.surname
            user_email = contact_entry.email
            user_phone = contact_entry.phone
            user_date = contact_entry.date
            user_guests = contact_entry.guests
            user_country = contact_entry.country
            user_message = contact_entry.message

            # Admin email details
            admin_email = "djaaangooo34@gmail.com"  # Replace with actual admin email
            subject_admin = "New Contact Form Submission"
            message_admin = f"""
            New contact form submission:

            Name: {user_name} {user_surname}
            Email: {user_email}
            Phone: {user_phone}
            Date of Contact: {user_date}
            Guests: {user_guests}
            Country: {user_country}
            Message: {user_message}
            """
            send_mail(subject_admin, message_admin, settings.DEFAULT_FROM_EMAIL, [admin_email])

            # User thank-you email
            subject_user = "Thank You for Contacting Us!"
            message_user = f"""
            Dear {user_name},

            Thank you for reaching out to us. We have received your message and will get back to you shortly.

            Here are the details you provided:
            Name: {user_name} {user_surname}
            Email: {user_email}
            Phone: {user_phone}
            Guests: {user_guests}
            Country: {user_country}

            Best Regards,
            HK Events 💕✨
            """
            send_mail(subject_user, message_user, settings.DEFAULT_FROM_EMAIL, [user_email])

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
