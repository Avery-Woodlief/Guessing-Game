print("This is a game of chance and luck or skill and intuition.")
print("The only way to win is to pick the lucky number.")
print("Player is given two tries...")
print("Do you have what it takes?")
proceed = input("Press enter to continue: ")

user_name = input("Please enter a name, player: ")
user_number = float(input("Enter your number: "))
guess_count = 1
guess_limit = 2
out_of_guesses = False
# Had to convert user_number to an integer by using the float command in order to compare to the number 5
# Default input is a string

# When the user's number is not 5, they have 2 tries to guess it or they lose.
while user_number != 5 and not (out_of_guesses):
    if guess_count < guess_limit:
        user_number = float(input("Please enter another number: "))
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Sorry " + user_name + ", you lost!")
else:
    print("Congratulaions " + user_name + ", you won!")
