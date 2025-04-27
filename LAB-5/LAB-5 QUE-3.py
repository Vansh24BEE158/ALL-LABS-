print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

# List of temperatures in Fahrenheit
fahrenheit_temps = [32, 50, 77, 104, 212]

# Convert Fahrenheit to Celsius
celsius_temps = [(temp - 32) * 5.0/9.0 for temp in fahrenheit_temps]

# Print the results
print("Temperatures in Fahrenheit:", fahrenheit_temps)
print("Equivalent temperatures in Celsius:", celsius_temps)
