# Weather-API

	Signing In and creating account and/& process to generate API Key.!!.




We follow this video link : 
https://www.youtube.com/watch?v=w-V1pMrGAjc

We get all the data about the weather forecast from the following site / URL .:- https://openweathermap.org/api


Now., we will go to the ‘ API ‘ tab., and currently we are accessing the following tab :-  Current Weather Data


So here., we can click on the API doc., which would show the API documentation.,!!..,,.. Here., / from there., we will.,/are planning to consider/take into account., the first API call.,::—                                             api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}


For this., we only need to give/enter the city name and the API KEY., hence we are choosing this one.,!!..


For the API key., we can generate it from this website itself., click on your account > My API Keys > and over here., you can generate an API key.!!.    ( based on your requirements .!!. )


However., note that we need to store the API Key in our local system and access it only via python using os., so that it remains confidential,.!!. Follow the following link video:-,..,                                                                  aa
https://www.youtube.com/watch?v=5iWhQWVXosUs


		For the security key., go to the folder where. The file has been stored and give the command ., nano .bash_profile ., and then follow the things as mentioned in the video., now the part which is not mentioned in the video is., after saving the changes ., press enter and exit, and then you will have to give the following command :— source .bash_profile    ., —> to make the changes commit/effective.!!.


now., when you will run the code., mentioning the API secret key., it will print the results.!!.


		So., now., coming back to the API application., we will write our own API link.,/ URL., based on the one that we have/had got from open weather . com ., which is mentioned in point number .(o) 4 .!!.   


         DATA INTERPRETATION><.,::—!!                                              
We have already seen the output in a raw/json format., Now., we will consider / refer to the API documentation that is provided by api.openweathermap.org., because that will help us to decode the data.,  
So if we go to API > Weather fields in API response > JSON ., so under this., we will have the documentation., of the API., and here we can clearly see the return values.,                                                         *{            
  "coord": {
    "lon": -122.08,
    "lat": 37.39
  },
  "weather": [
    {
      "id": 800,
      "main": "Clear",
      "description": "clear sky",
      "icon": "01d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 282.55,
    "feels_like": 281.86,
    "temp_min": 280.37,
    "temp_max": 284.26,
    "pressure": 1023,
    "humidity": 100
  },
  "visibility": 16093,
  "wind": {
    "speed": 1.5,
    "deg": 350
  },
  "clouds": {
    "all": 1
  },
  "dt": 1560350645,
  "sys": {
    "type": 1,
    "id": 5122,
    "message": 0.0139,
    "country": "US",
    "sunrise": 1560343627,
    "sunset": 1560396563
  },
  "timezone": -25200,
  "id": 420006353,
  "name": "Mountain View",
  "cod": 200
  }                         
     
Now., for our reference., we have not chosen all the fields for our program., and/but have chosen temp., weather_desc., hmdt., wind_spd.,!!….
Note that here short for of weather locations are also accepted.,!!… like., if we give del instead of delhi/Delhi/DELHI., then also it will accept.!!. The thing.,!!….,,..

                                                                                                                          



