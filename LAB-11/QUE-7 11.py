print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")


class Weather:
    def __init__(self, temperature, humidity, wind_speed, precipitation):
       
        self.weather_parameters = [temperature, humidity, wind_speed, precipitation]
    

    def __contains__(self, item):
        return item in self.weather_parameters

    def display(self):
        return f"Weather Parameters: Temperature: {self.weather_parameters[0]}°C, Humidity: {self.weather_parameters[1]}%, Wind Speed: {self.weather_parameters[2]} km/h, Precipitation: {self.weather_parameters[3]} mm"


weather = Weather(30, 60, 15, 5) 

if 30 in weather:  
    print("30°C is present in the weather parameters.")
else:
    print("30°C is not present in the weather parameters.")

if 100 in weather: 
    print("100% Humidity is present in the weather parameters.")
else:
    print("100% Humidity is not present in the weather parameters.")


print(weather.display())
