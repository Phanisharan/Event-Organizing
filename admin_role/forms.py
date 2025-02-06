from django import forms
from Eventapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = User        
        fields = ['username', 'password1', 'password2']

class CardForm(forms.ModelForm): 
        class Meta:        
            model = Card        
            fields = '__all__'

class GalleryForm(forms.ModelForm): 
    class Meta:        
        model = Gallery        
        fields = '__all__'
    
class ServicesForm(forms.ModelForm): 
    class Meta:        
        model = Services        
        fields = '__all__'
        
class PackagesForm(forms.ModelForm): 
    class Meta:        
        model = Packages        
        fields = '__all__'
        
class CoupleMomentsForm(forms.ModelForm): 
    class Meta:        
        model = CoupleMoments        
        fields = '__all__'

class WeddingGalleryForm(forms.ModelForm): 
    class Meta:        
        model = WeddingGallery        
        fields = '__all__'

class CoupleMomentsForm(forms.ModelForm): 
    class Meta:        
        model = CoupleMoments        
        fields = '__all__'
        
class VenueForm(forms.ModelForm): 
    class Meta:        
        model = Venue        
        fields = '__all__'
        
class OcassionForm(forms.ModelForm): 
    class Meta:        
        model = Ocassion        
        fields = '__all__'
        
class DecorationForm(forms.ModelForm): 
    class Meta:        
        model = Decoration        
        fields = '__all__'
        
class PhotographyForm(forms.ModelForm): 
    class Meta:        
        model = Photography        
        fields = '__all__'
