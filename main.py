# Main Stories

# ●	(5 points): As a developer, I want to make at least three commits with descriptive messages 
# ●	(5 points):  As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment in their own separate Lists. 
# ●	(5 points): As a user, I want a destination to be randomly selected for my day trip. 
# ●	(5 points): As a user, I want a restaurant to be randomly selected for my day trip
# ●	(5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 
# ●	(5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.
# ●	(15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.
# ●	(10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.
# ●	(10  points): As a user, I want to display my completed trip in the console
# ●	(5 points): Single Responsibility: As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing! 
import random
destinations = ["Japan", "Korea", "China", "Taiwan", "Vietnam"]
restaurants = ["Hotspicydip", "Canes"]
transportation = ["Car", "Train"]
entertainment = ["Badminton", "Movies"]
def randomizer():
    return [
    random.choice(destinations),
    random.choice(restaurants),
    random.choice(transportation),
    random.choice(entertainment)
    ]
trip1 = randomizer()
def starting():
    print(f"Your day trip will compose of: \nDestination: {trip1[0]} \nRestaurant: {trip1[1]} \nTransportation: {trip1[2]} \nEntertainment: {trip1[3]}")  
def changes():
    temp = False
    while temp == False:
        change = input("Would you like to change anything in your day trip? Y or N or Everything\n")
        if change == "Y":
            which_one = input("What would you like to change? Please select one at a time: \nDestinations, Restaurants, Transportation, or Entertainment?\n")
            choices(which_one)
        if change == "Everything":
            global trip1 
            trip1 = randomizer()
            print(f"Your new day trip will compose of: \nDestination: {trip1[0]} \nRestaurant: {trip1[1]} \nTransportation: {trip1[2]} \nEntertainment: {trip1[3]}")   
        else: 
            print(f"Your day trip will compose of: \nDestination: {trip1[0]} \nRestaurant: {trip1[1]} \nTransportation: {trip1[2]} \nEntertainment: {trip1[3]}")
            confirmation = input("Are you satisfied with your day trip? Y or N\n")
            if confirmation == "Y":
                temp = True
            else:
                temp = False
def choices(which_one):
    if which_one == "Destinations":
        trip1[0] = random.choice(destinations)
        print(f"Your new destination has been updated to {trip1[0]}")
    if which_one == "Restaurants":
        trip1[1] = random.choice(restaurants)
        print(f"The new restaurant has been updated to {trip1[1]}")
    if which_one == "Transportation":
        trip1[2] = random.choice(transportation)
        print(f"The new mode of transportation has been updated to {trip1[2]}")
    if which_one == "Entertainment":  
        trip1[3] = random.choice(entertainment)
        print(f"The new means of entertainment has been updated to {trip1[3]}") 

def final():
    print(f"Congratulations on your day trip! Your day trip will compose of: \nDestination: {trip1[0]} \nRestaurant: {trip1[1]} \nTransportation: {trip1[2]} \nEntertainment: {trip1[3]}")        




def day_trip_generator():
    trip1 = randomizer()
    starting()
    changes()
    final()



day_trip_generator()   