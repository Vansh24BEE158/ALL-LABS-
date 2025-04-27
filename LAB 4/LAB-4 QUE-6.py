print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

print("24 Hours of the Day:")

for hour in range(0, 24):
    if hour == 0:
        print("12:00 Midnight")
    elif hour == 12:
        print("12:00 Noon")
    elif hour < 12:
        print(f"{hour}:00 AM")
    else:
        print(f"{hour - 12}:00 PM")
