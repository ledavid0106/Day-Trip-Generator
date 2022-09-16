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
    print(f"Your day trip will compose of: \n{des_random} as your destination, \n{res_random} as your restaurant, \n{trans_random} as your means of transportation, \nand {ent_random} as your entertainment.")
    temp = False
    while temp == False:
        change = input("Would you like to change anything in your day trip? Yes or No\n")
        if change == "Yes":
            which_one = input("What would you like to change? Please select one at a time: \nDestinations, Restaurants, Transportation, or Entertainment?\n")
            if which_one == "Destinations":
                des_random = random.choice(destinations)
                print("Your new destination has been updated")
            if which_one == "Restaurants":
                res_random = random.choice(restaurants)
                print("The new restaurant has been updated")
            if which_one == "Transportation":
                trans_random = random.choice(transportation)
                print("The new mode of transportation has been updated")
            if which_one == "Entertainment":  
                ent_random = random.choice(entertainment)
                print("The new means of entertainment has been updated")     
        else: 
            print(f"Your new day trip will compose of: \n{des_random} as your destination, \n{res_random} as your restaurant, \n{trans_random} as your means of transportation, \nand {ent_random} as your entertainment.")
            confirmation = input("Are you satisfied with your new day trip? Yes or No\n")
            if confirmation == "Yes":
                temp = True
            else:
                temp = False




day_trip_generator()   