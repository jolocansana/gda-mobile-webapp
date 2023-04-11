import requests

url = "https://meteostat.p.rapidapi.com/stations/nearby"

querystring = {"lat":"1.3521","lon":"103.8198"}

headers = {
	"X-RapidAPI-Key": "6fd217084emsh5d7bced4c2cbf13p15fe33jsn61abc617ad25",
	"X-RapidAPI-Host": "meteostat.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)