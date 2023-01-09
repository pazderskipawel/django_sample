from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(label='Wyszukaj w Wikipedii (pl)')
