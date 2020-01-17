#commenting
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    import json
    import requests

    if request.method == "POST":
        zip = request.POST['zip']
        #api_request = requests.get("http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode="+zip+"&date=2020-01-17&distance=25&API_KEY=36516356-21F8-4B9B-8DB5-4D048D4E5DFA")
        api_request = requests.get("https://api.waqi.info/feed/"+zip+"/?token=f5c3022d3f561a3c3dc4e491cce003d2e5dc61a4")
        try:
            api = json.loads(api_request.content)

        except Exception as e:
            api="api error.."
            #https://api.waqi.info/feed/bangalore/?token=f5c3022d3f561a3c3dc4e491cce003d2e5dc61a4
        return render(request, 'home.html', {'api':api})

        return render(request, 'home.html', {'zip':zip})
    else:
        api_request = requests.get("https://api.waqi.info/feed/bangalore/?token=f5c3022d3f561a3c3dc4e491cce003d2e5dc61a4")
        #api_request = requests.get("http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=20001&date=2020-01-17&distance=25&API_KEY=36516356-21F8-4B9B-8DB5-4D048D4E5DFA")
        try:
            api = json.loads(api_request.content)

        except Exception as e:
            api="api error.."
            #https://api.waqi.info/feed/bangalore/?token=f5c3022d3f561a3c3dc4e491cce003d2e5dc61a4
        return render(request, 'home.html', {'api':api})

def about(request):
    return render(request, 'about.html', {})