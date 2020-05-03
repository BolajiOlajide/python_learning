import datetime as DT


# get today's date
print(DT.date.today())

# construct a date - format is Year, Month, Day
print(DT.date(2014, 8, 20))
# you can also do this by passing in keyword args
print(DT.date(year=2014, month=8, day=20))


# construct the time (order = hour, minute, second, microsecond)
print(DT.time(23, 12, 45, 345123))
# you can do this using keyword args if you forget the order
print(DT.time(hour=23, minute=12, second=45, microsecond=345123))


# DateTime is a combination of both day and time
# to get the current datetime
print(DT.datetime.now())
# OR
print(DT.datetime.today())

# if you create a separate date and time you can combine them using the
# combine method available in the datetime class
d = DT.date(2017, 4, 13)
t = DT.time(8, 15)

dt = DT.datetime.combine(d, t)
print(dt)

# timedelta is used to calculate the duration between two date/datetime
# instances
# to calculate three weeks from the current date
dt = DT.date.today() + DT.timedelta(weeks=3)
print(dt)

# the constructor for timedelta accepts the following arguments
# which you're advised to always make positional
"""
- days
- seconds
- microseconds
- milliseconds
- minutes
- hours
- weeks
"""

# it can't be used to perform arithmetic calcs on time instances

# to create a date time object that's timezone aware for GMT +0100
cet = DT.timezone(DT.timedelta(hours=1), "CET")  # CET == GMT +1

# calculate departure and arrival time using the timezone created above
departure = DT.datetime(year=2018, month=1, day=7, hour=11, minute=30, tzinfo=cet)

arrival = DT.datetime(
    year=2018, month=1, day=7, hour=13, minute=5, tzinfo=DT.timezone.utc
)
# specify utc timezone

print(arrival - departure)  # this is how long the flight took
