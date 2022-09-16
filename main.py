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
destinations = ["Japan", "Korea"]
restaurants = ["Hotspicydip", "Canes"]
transportation = ["Car", "Train"]
entertainment = ["Badminton", "Movies"]
# print(random.choice(destinations))
def day_trip_generator():
    des_random = random.choice(destinations)
    res_random = random.choice(restaurants)
    trans_random = random.choice(transportation)
    ent_random = random.choice(entertainment)
    print(f"Your day trip will compose of: \nDestination: {des_random} \nRestaurant: {res_random} \nTransportation: {trans_random} \nEntertainment: {ent_random}")
    temp = False
    while temp == False:
        change = input("Would you like to change anything in your day trip? Y or N or Everything\n")
        if change == "Y":
            which_one = input("What would you like to change? Please select one at a time: \nDestinations, Restaurants, Transportation, or Entertainment?\n")
            if which_one == "Destinations":
                des_random = random.choice(destinations)
                print(f"Your new destination has been updated to {des_random}")
            if which_one == "Restaurants":
                res_random = random.choice(restaurants)
                print(f"The new restaurant has been updated to {res_random}")
            if which_one == "Transportation":
                trans_random = random.choice(transportation)
                print(f"The new mode of transportation has been updated to {trans_random}")
            if which_one == "Entertainment":  
                ent_random = random.choice(entertainment)
                print(f"The new means of entertainment has been updated to {ent_random}") 
        if change == "Everything":
            des_random = random.choice(destinations)
            res_random = random.choice(restaurants)
            trans_random = random.choice(transportation)
            ent_random = random.choice(entertainment)
            print(f"Your new day trip will compose of: \nDestination: {des_random} \nRestaurant: {res_random} \nTransportation: {trans_random} \nEntertainment: {ent_random}")   
        else: 
            print(f"Your new day trip will compose of: \nDestination: {des_random} \nRestaurant: {res_random} \nTransportation: {trans_random} \nEntertainment: {ent_random}")
            confirmation = input("Are you satisfied with your new day trip? Y or N\n")
            if confirmation == "Y":
                temp = True
            else:
                temp = False
    print(f"Congratulations on your day trip! Your day trip will compose of: \nDestination: {des_random} \nRestaurant: {res_random} \nTransportation: {trans_random} \nEntertainment: {ent_random}")    



day_trip_generator()   