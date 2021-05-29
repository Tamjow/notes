import datetime

from django import forms
from django.forms import ModelForm

from .models import Note


class DateInput(forms.DateInput):
    input_type = 'date'


class NoteForm(ModelForm):
    """A form for saving the expiration date and the password for a single note."""
    class Meta:
        model = Note
        fields = ['expiration_date', 'password']
        widgets = {
            'expiration_date': DateInput(attrs={'min': str(datetime.date.today() + datetime.timedelta(days=1))}),
            'password': forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Password'}),
        }

    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        self.label_suffix = ''
        self.fields['expiration_date'].required = False
        self.fields['expiration_date'].label = 'Expiration Date'
        self.fields['password'].required = False
        self.fields['password'].label = 'Password'
