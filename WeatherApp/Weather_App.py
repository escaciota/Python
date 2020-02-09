import requests
import json
import pprint

accuweatherAPIKey = 'OIAZsqrvY1LWhvA3faMYqNGDTwFLEtji'

r = requests.get('http://www.geoplugin.net/json.gp')

if r.status_code != 200:
    print("It wasn't possible to retrieve your location")
else:
    localizacao = json.loads(r.text)
    lat = localizacao['geoplugin_latitude']
    long = localizacao['geoplugin_longitude']

    LocationAPIUrl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey="+accuweatherAPIKey+"&q="+lat+"%2C"+long+"&language=pt-br"

    r2 = requests.get(LocationAPIUrl)

    if r2.status_code != 200:
        print("It wasn't possible to retrieve your location")
    else:
        locationresponse = json.loads(r2.text)
        nomeLocal = locationresponse['LocalizedName'] + "," +  locationresponse['AdministrativeArea']['LocalizedName'] + ". " + locationresponse['Country']['LocalizedName']
        codigoLocal = locationresponse['Key']

        ConditionsAPIUrl = "http://dataservice.accuweather.com/currentconditions/v1/"+codigoLocal+"?apikey="+accuweatherAPIKey+"&language=pt-br"

        r3 = requests.get(ConditionsAPIUrl)

        if r3.status_code != 200:
            print("It wasn't possible to retrieve your location")
        else:
            CurrentConditionResponse = json.loads(r3.text)
            TextoClima = CurrentConditionResponse[0]['WeatherText']
            TempF = str(CurrentConditionResponse[0]['Temperature']['Imperial']['Value'])
            UnitF = str(CurrentConditionResponse[0]['Temperature']['Imperial']['Unit'])
            TempC = str(CurrentConditionResponse[0]['Temperature']['Metric']['Value'])
            UnitC = str(CurrentConditionResponse[0]['Temperature']['Metric']['Unit'])
            print("Obtendo clima do local:", nomeLocal)
            print("Clima no momento: ", TextoClima)
            print("Temperatura em F: ", TempF, UnitF)
            print("Temperatura em C: ", TempC, UnitC)