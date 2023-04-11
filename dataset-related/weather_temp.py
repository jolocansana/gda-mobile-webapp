import requests

url = "https://meteostat.p.rapidapi.com/stations/hourly"

querystring = {"station":"48692","start":"2023-02-14","end":"2023-02-14"}

headers = {
	"X-RapidAPI-Key": "6fd217084emsh5d7bced4c2cbf13p15fe33jsn61abc617ad25",
	"X-RapidAPI-Host": "meteostat.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)