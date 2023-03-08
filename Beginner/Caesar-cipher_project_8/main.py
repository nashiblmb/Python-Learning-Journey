# Caesar Cipher - Project 8
from art import logo
print(logo)

# Encrypts the given text using the given shift and alphabet
def encrypt(text, shift, alphabet):

    # Convert the plain text to a list of characters
    plain_text = list(text)

    # Initialize an empty list to hold the encrypted text
    cipher_text = []

    # Iterate over each character in the plain text
    for i in range(len(plain_text)):

        # If the character is a space, append it to the cipher text
        if plain_text[i] == " ":
            cipher_text.append(" ")

        # If the character is a letter, encrypt it using the given shift and append it to the cipher text
        elif plain_text[i].isalpha():
            cipher_text.append(alphabet[(alphabet.index(plain_text[i])+shift)%25])

        # Otherwise, append the character to the cipher text unchanged
        else:
            cipher_text.append(plain_text[i])

    # Print the encrypted text
    return cipher_text

# Decrypts the given text using the given shift and alphabet
def decrypt(text, shift, alphabet):

    # Convert the cipher text to a list of characters
    cipher_text = list(text)

    # Initialize an empty list to hold the decrypted text
    plain_text = []

    # Iterate over each character in the cipher text
    for i in range(len(cipher_text)):

        # If the character is a space, append it to the decrypted text
        if cipher_text[i] == " ":
            plain_text.append(" ")

        # If the character is a letter, decrypt it using the given shift and append it to the decrypted text
        elif cipher_text[i].isalpha():
            plain_text.append(alphabet[(alphabet.index(cipher_text[i])-shift)%25])

        # Otherwise, append the character to the decrypted text unchanged
        else:
            plain_text.append(cipher_text[i])

    # Return the decrypted text
    return plain_text

# Asks the user if they want to play again
def replay():
    while True:
        # Ask the user if they want to play again
        play_again = input("Do you want to try again? (Yes/No)\n").lower()

        # If the user wants to play again, return True
        if play_again == 'y' or play_again == 'yes':
            return True
        
        # If the user does not want to play again, return False
        elif play_again == 'n' or play_again == 'no':
            return False
        
        # If the user inputs an invalid response, ask again
        else:
            print("Invalid input, please enter 'y' or 'n'.\n")
            continue    


# Define the alphabet as a list of lowercase letters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Start the game loop
game_status = True
while game_status == True:

    # Ask the user whether they want to encrypt or decrypt
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction not in ['encode', 'decode']:
            print("Invalid input, please enter either 'encode' or 'decode'.")
        else:
            break

    # Ask the user for the text to encrypt or decrypt
    while True:
        text = input("Type your message:\n").lower()
        if not text:
            print("Invalid input, please enter a non-empty message.")
        else:
            break

    # Ask the user for number of shifts
    while True:
        try:
            shift = int(input("Type the shift number:\n"))
            break
        except ValueError:
            print("Invalid input, please enter an integer.")


    # If user chose to encode, start encrypt function
    if direction == "encode":
        encrypted_text = encrypt(text, shift, alphabet)
        print(f"The ciphertext: {''.join(encrypted_text)}")

    # If user chose to decode, start decrypt function
    elif direction == "decode":
        decrypted_text = decrypt(text, shift, alphabet)
        print(f"The plaintext: {''.join(decrypted_text)}")

    # Start replay function to check if user wants to try again
    game_status = replay()