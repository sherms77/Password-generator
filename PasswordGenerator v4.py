'''
This is a password generator app.
It will generate a random password that is 10 characters long.
'''

# 050920: Used random instead of the secrets module in passwordGen function.

import random, time, string # secrets
choice = ''

print("WELCOME TO MY PASSWORD GENERATOR \n")

def mainMenu():
    choice = input("Press y and enter to generate a password or \nPress q and enter to quit: ")
    if choice == 'y':
        passwordGen()
    elif choice == 'q':
        exit()
        
def passwordGen():
    characters = string.ascii_letters + string.digits + string.punctuation
    print("\nA password made up of 10 characters will now be generated for you.")
    print("\nPassword is generating...\n")
    time.sleep(1)
    combined = ''.join(random.sample(characters, 10)) 
    print(combined)
    print("\nDo you want to generate another password?")

mainMenu()

while choice != 'q':
    mainMenu() 
