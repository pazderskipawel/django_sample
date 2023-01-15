import requests
from django.shortcuts import render
from itertools import combinations
from wiki.forms import SearchForm


# Create your views here.
def wiki_view(request):
    if request.method == 'POST':
        # process form submission
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            words = query.split()  # split the query into a list of search terms
            terms = []
            for i in range(1, len(words) + 1):
                for comb in combinations(words, i):
                    terms.append(" ".join(comb).capitalize())
            print(terms)
            # https://www.mediawiki.org/wiki/API:Query <- documentation
            url = f"https://pl.wikipedia.org/w/api.php?action=query&format=json&utf8=1&formatversion=2&prop=extracts&exintro=1&explaintext=1&titles={'|'.join(terms)}"
            response = requests.get(url)
            data = response.json()
            print(data)
            results = []
            if 'pages' in data['query']:
                found_terms = set()
                for page in data['query']['pages']:
                    print(page)
                    if 'extract' in page:
                         extract = page['extract']
                         title = page['title']
                         found_terms.add(title)
                         results.append({'term': title, 'extract': extract})
                    else:
                         continue
                not_found_terms = set(terms) - found_terms
                for term in not_found_terms:
                    results.append({'term': term, 'extract': 'Nie znaleziono wyniku'})
            else:
                # handle the case where there are no search results
                results.append({'term': 'Nie znaleziono wyniku', 'extract': 'Nie znaleziono wyniku'})
        else:
            results = []
    else:
        # display the form
        form = SearchForm()
        results = []
    return render(request, 'wiki/wiki.html', {'form': form, 'results': results})
