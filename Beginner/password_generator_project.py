#Password Generator Project
import random

#function takes three variables and combines them to a list before shuffling them and converting to a str
def join_characters(letters, symbols, numbers):
    password = []

    #extends password list with the three given variables
    password.extend(letters)
    password.extend(symbols)
    password.extend(numbers)

    #shuffles the password list
    random.shuffle(password)

    #converts list into string
    joined_password = "".join(map(str,password))

    #returns converted string
    return joined_password

#function to choose characters and length
def password_generation():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    #askes for input of character amount
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    #randomises each character choice according to amount chosen
    password_letters = random.choices(letters, k=nr_letters)
    password_symbols = random.choices(symbols, k=nr_symbols)
    password_numbers = random.choices(numbers, k=nr_numbers)
    
    #returns the function result for joining the characters together
    return join_characters(password_letters, password_symbols, password_numbers)

print("Welcome to the PyPassword Generator!")
print("-----------------------------------------")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#Start
generated_password = password_generation()
print("-----------------------------------------")
print(f"Your password is '{generated_password}'")
print("-----------------------------------------")
input("End of Program!\n")