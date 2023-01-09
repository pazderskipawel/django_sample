import requests
from django.shortcuts import render

from wiki.forms import SearchForm


# Create your views here.
def wiki_view(request):
    if request.method == 'POST':
        # process form submission
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            terms = query.split()  # split the query into a list of search terms
            results = []
            for term in terms:
                url = f'https://pl.wikipedia.org/w/api.php?action=query&format=json&utf8=1&formatversion=2&prop=extracts&exlimit=1&exintro=1&explaintext=1&titles={term}'
                response = requests.get(url)
                data = response.json()
                if 'pages' in data['query']:
                    # handle the case where there are search results
                    if isinstance(data['query']['pages'], list):
                        # handle the case where data['query']['pages'] is a list
                        for page in data['query']['pages']:
                            if 'extract' in page:
                                extract = page['extract']
                            else:
                                # handle the case where the 'extract' field is not present
                                extract = 'Nie znaleziono wyniku'
                            results.append({'term': term, 'extract': extract})
                    else:
                        # handle the case where data['query']['pages'] is a dictionary
                        if 'extract' in next(iter(data['query']['pages'].values())):
                            extract = next(iter(data['query']['pages'].values()))['extract']
                        else:
                            # handle the case where the 'extract' field is not present
                            extract = 'Nie znaleziono wyniku'
                        results.append({'term': term, 'extract': extract})
                else:
                    # handle the case where there are no search results
                    results.append({'term': term, 'extract': 'Nie znaleziono wyniku'})
        else:
            results = []
    else:
        # display the form
        form = SearchForm()
        results = []
    return render(request, 'wiki/wiki.html', {'form': form, 'results': results})
