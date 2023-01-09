from django.forms import ModelForm, widgets
from django.utils.datetime_safe import datetime

from .models import Note

class NewNoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'date', 'content']
        widgets = {
            'date': widgets.DateInput(attrs={'type': 'date', 'value': datetime.now().strftime("%Y-%m-%d")})
        }