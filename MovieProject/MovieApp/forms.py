from django import forms;
from MovieApp.models import Movies

class MoviesForm(forms.ModelForm):
    #no-separate fields are required(taken from model-Movies-class)
    class Meta:
        model=Movies
        fields='__all__'
