import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    # defines letters numbers and special characters in variables
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    #loads the letters into a variable
    characters = letters
    #if the parameters for no.s and specials are true add
    #them to the list of characters
    if numbers:
        characters +=digits
    if special_characters:
        characters+=special

    pwd =""
    meet_criteria=False
    has_number=False
    has_special=False
    #while the criteria specified is not met and the length 
    # is less than that required run the code below
    while not meet_criteria or len(pwd) < min_length:
        new_char = random.choice(characters) #add random from list to a new_char var
        pwd += new_char #add the new var to the password
        #if the new character is a digit or a special char. set true for respective
        if new_char in digits:
            has_number=True
        elif new_char in special:
            has_special=True
        #initialise the criteria as true and try to prove to be false otherwise true
        meet_criteria=True
        #if user chose numbers to be available 
        # and a number is not there set criteria as false if not skip
        if numbers:
            meets_criteria=has_number
        #check if criteria is true if not then false. if true check if password
        #has special then set to true and exit out loop if length is satisfied
        if special_characters:
            meet_criteria=meets_criteria and has_special
    
    return pwd

#user input
min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want a number (y/n)?").lower()=="y"
has_special=input("Do you want special characters (y/n)? ").lower()=="y"
pwd=generate_password(min_length,has_number,has_special)
print(pwd)
#thank u