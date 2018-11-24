from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from .models import Cadastro


class MeasureForm(forms.ModelForm):
    file_csv = forms.FileField(required=False)
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Description'})) # TextArea

    def clean_title(self):
        title = self.cleaned_data['title']
        if Cadastro.objects.filter(title=title).exists():
            raise ValidationError("title is already in use!")
        return title


    class Meta:
        model = Cadastro
        fields = ('title', 'description','file_csv')