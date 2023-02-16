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

    def __init__(self, *args, **kwargs):
        super(NewNoteForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'