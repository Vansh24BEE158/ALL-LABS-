print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")


class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalize_time()

    def normalize_time(self):
     
        if self.seconds >= 60:
            self.minutes += self.seconds // 60
            self.seconds = self.seconds % 60
        if self.minutes >= 60:
            self.hours += self.minutes // 60
            self.minutes = self.minutes % 60


    def __add__(self, other):
        total_seconds = self.to_seconds() + other.to_seconds()
        return Time.from_seconds(total_seconds)


    def __sub__(self, other):
        total_seconds = self.to_seconds() - other.to_seconds()
        return Time.from_seconds(total_seconds)

   
    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


    @classmethod
    def from_seconds(cls, total_seconds):
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return cls(hours, minutes, seconds)


    def display(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"


    def difference(self, other):
        total_seconds = abs(self.to_seconds() - other.to_seconds())
        return Time.from_seconds(total_seconds)

time1 = Time(2, 45, 50) 
time2 = Time(1, 30, 30) 

result_add = time1 + time2
print(f"Sum of {time1.display()} and {time2.display()} is {result_add.display()}")

result_sub = time1 - time2
print(f"Difference between {time1.display()} and {time2.display()} is {result_sub.display()}")


result_diff = time1.difference(time2)
print(f"Absolute difference between {time1.display()} and {time2.display()} is {result_diff.display()}")

