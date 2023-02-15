from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(label='Search in polish wikipedia: ')
