from django.contrib import admin
from .models import *

# Register your models here.

class CardAdmin(admin.ModelAdmin):
    list_display = ['marraige_date', 'couple_names', 'card_images']

admin.site.register(Card, CardAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ['gallery_images']

admin.site.register(Gallery, GalleryAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone', 'email', 'message']

admin.site.register(Contact, ContactAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_image', 'service_name']

admin.site.register(Services, ServiceAdmin)

class PackagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'detail_description', 'price']

admin.site.register(Packages, PackagesAdmin)

class CoupleMomentsAdmin(admin.ModelAdmin):
    list_display = ['names', 'couple_image']

admin.site.register(CoupleMoments, CoupleMomentsAdmin)