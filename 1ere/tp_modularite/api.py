import requests
API_KEY = "439d4b804bc8187953eb36d2a8c26a02"
def get_weather(api_key, location):
    url = f"https://samples.openweathermap.org/data/2.5/weather?zip={location}&appid={api_key}"
    r = requests.get(url)
    return r.json()

zip = int(input('ZIP : '))
print(get_weather(API_KEY, zip)['weather'][0]['main'])