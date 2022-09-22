from data import *
import random

def randomizer(city):
    return [
    random.choice(city["Restaurants"]),
    ]

print(randomizer(Irvine))