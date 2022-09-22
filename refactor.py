from data import *
import random

def randomizer(city):
    return [
    random.choice(city["Restaurants"]),
    random.choice(city["Transportation"]),
    random.choice(city["Entertainment"])
    ]
Irvine_Trip = randomizer(Irvine)
Rowland_Trip = randomizer(Rowland_Heights)
LA_Trip = randomizer(LA)
SD_Trip = randomizer(SD)

# List = [Irvine_Trip, Rowland_Heights, LA_Trip, SD_Trip]

def starting():
    city = input("What city would you like to go to? Irvine, Rowland Heights, LA, SD\n ")
    return city

def trip(city):
    if city == "Irvine":
        trip1 = Irvine_Trip
    if city == "Rowland Heights":
        trip1 = Rowland_Trip
    if city == "LA":
        trip1 = LA_Trip
    if city == "SD":
        trip1 = SD_Trip
    print(f"Your {city} trip will compose of: \nRestaurant: {trip1[1]} \nTransportation: {trip1[2]} \nEntertainment: {trip1[3]}")
def end():
    starting()
    trip(starting())

end()
