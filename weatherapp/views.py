from django.shortcuts import render
import json
import urllib.request

from django.template import context

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=9f5432d5098287728e3913d28a965f60').read()
        res_json_data = json.loads(res)
        data = {
            # 'city':city,
            'country_code': str(res_json_data['sys']['country']),
            'coordinate': str(res_json_data['coord']['lon']) + ' ' + str(res_json_data['coord']['lat']),
            'temperature': str(res_json_data['main']['temp']),
            'pressure': str(res_json_data['main']['pressure']),
            'humidity': str(res_json_data['main']['humidity']),
        }
        kel = float(data['temperature'])
        cel = kel-273.15
    else:
        city = ''
        cel = ''
        data = {}
    return render(request, 'index.html', {'city':city, 'cel':cel, 'data':data})