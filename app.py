import requests
import os
from datetime import datetime

user_api = os.environ['KEY']
location = input("Enter the city name: ")

## api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key} ##

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api  ## so this api link that we create is based on the above link that we get from the open weather site.!!.
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#print(api_data)

## After printing the api_data., we will get the value in the form of JSON., which would look somewhat like this:--.,!! 
'''
siddharthachakraborty@Siddharthas-Air Real-time Weather REST API % python3 app.py
Enter the city name: Delhi
{'coord': {'lon': 77.2167, 'lat': 28.6667}, 'weather': [{'id': 721, 'main': 'Haze', 'description': 'haze', 'icon': '50n'}], 'base': 'stations', 'main': {'temp': 297.15, 'feels_like': 296.91, 'temp_min': 297.15, 'temp_max': 297.15, 'pressure': 1010, 'humidity': 53}, 'visibility': 3000, 'wind': {'speed': 2.06, 'deg': 90}, 'clouds': {'all': 40}, 'dt': 1616353615, 'sys': {'type': 1, 'id': 9165, 'country': 'IN', 'sunrise': 1616374371, 'sunset': 1616418190}, 'timezone': 19800, 'id': 1273294, 'name': 'Delhi', 'cod': 200}
'''

if api_data['cod']=='404':		## If some wromg city name is entered.,!!.... hence we are giving some random key name which we know for sure does not / will not exist in the dictionary.!!.
	print("Invalid City : {}, Please check the city name ".format(location))
else:
	#create variables to store and display data
	temp_city = ((api_data['main']['temp']) - 273.15)		## accessing the api_data as a dictionary., and since the value of the temperature is in kelvin., we are converting it into celsius.!!.
	weather_desc = api_data['weather'][0]['description']
	hmdt = api_data['main']['humidity']
	wind_spd = api_data['wind']['speed']
	date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

	print ("-------------------------------------------------------------")
	print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
	print ("-------------------------------------------------------------")

	print ("Current temperature is: {:.2f} deg C".format(temp_city))
	print ("Current weather desc  :",weather_desc)
	print ("Current Humidity      :",hmdt, '%')
	print ("Current wind speed    :",wind_spd ,'kmph')