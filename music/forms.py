from django import forms
from .models import Song, Artist
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AddSongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['name', 'Date_of_release','cover','artist']
        labels = {
            'cover': 'Artwork'
        }

class AddArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = "__all__"

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
