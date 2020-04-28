#we are going to use open weather map api make this project
#pip install pyown
#here we will learn ho to fetch json data using its api key
#api key of openweather: 36768002e8b918d8a071d6c331ab713c
import requests
#this is the way by which we open the json data from api key
api_address="http://api.openweathermap.org/data/2.5/weather?appid=36768002e8b918d8a071d6c331ab713c&q="
city=input("City name:")


url=api_address+city  

json_data= requests.get(url).json()    # here we are getting the complete json data using request.get method
print(json_data)
#now we are performing operation on that json data
#temperature
fromatted_data_temp=json_data['main']['temp']
print(f"Temperature:{fromatted_data_temp} F") 

#humidity
fromatted_data_hum=json_data['main']['humidity']
print(f"humidity:{fromatted_data_hum} %") 

#we can also print mny more parameter using the json information from json_data



