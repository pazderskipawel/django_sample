from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from geopy.geocoders import Nominatim
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request


def get_location(city):
    geolocator = Nominatim(user_agent="django_sample")
    location = geolocator.geocode(city)
    return str(location.latitude), str(location.longitude)


def weather_view(request):
    if request.method == 'POST':
        city = request.POST['city']
        lat, lon = get_location(city)
        # source contain JSON data from API
        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?lat='
            + lat + '&lon=' + lon + '&units=metric&appid=APPID').read()

        # converting JSON data to a dictionary
        list_of_data = json.loads(source)

        # data for variable list_of_data
        data = {
            "name": str(list_of_data['name']),
            "country_code": str(list_of_data['sys']['country']),
            "lon": str(list_of_data['coord']['lon']),
            "lat": str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'C',
            "pressure": str(list_of_data['main']['pressure']),
        }
        print(data)
    else:
        data = {}
    return render(request, "weather/index.html", data)
