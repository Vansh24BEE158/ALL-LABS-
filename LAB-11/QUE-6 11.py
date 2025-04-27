
print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
 
    def __eq__(self, other):
        if isinstance(other, Date):
            return (self.day == other.day) and (self.month == other.month) and (self.year == other.year)
        return False  
    

    def display(self):
        return f"{self.day:02}/{self.month:02}/{self.year}"


date1 = Date(15, 8, 2021) 
date2 = Date(15, 8, 2021) 
date3 = Date(16, 8, 2021) 

if date1 == date2:
    print(f"{date1.display()} is the same as {date2.display()}")
else:
    print(f"{date1.display()} is not the same as {date2.display()}")


if date1 == date3:
    print(f"{date1.display()} is the same as {date3.display()}")
else:
    print(f"{date1.display()} is not the same as {date3.display()}")
