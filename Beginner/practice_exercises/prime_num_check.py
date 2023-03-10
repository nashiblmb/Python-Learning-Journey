def prime_checker(number):
    if number == 1:
        print(f"{number} is not a prime number")
    elif number > 1:
        for numbers in range(2, number):
            if number % numbers == 0:
                print(f"{number} is not a prime number")
                break
        else:
            print(f"{number} is a prime number")
            

            

n = int(input("Check this number: "))
prime_checker(n)