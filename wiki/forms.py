from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(label='Search in polish wikipedia')
    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'