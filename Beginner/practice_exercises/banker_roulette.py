#Practice exercise creating a banker roulette without use of random.choice()
import random

names_string = input("Please enter names of participants with comma seperating the names: ")
names_list = names_string.split(", ")

max_index = random.randint(0, (len(names_list)))

print(f"{names_list[max_index]} is going to buy the meal today!")
