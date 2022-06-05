import random

range = input("Type a number: ")  # are varible is "top_of_range"

if range.isdigit():  # the "isdigit" is used if someone is trying to put something that isnt a number in the "int" statement.
    # in python if you want a number to be printed you cant put quotation marks because it wont know its a number so we must use "int" an it will convert the string into a numeric representation.
    range = int(range)

    if range <= 0:  # the "<=" means less then or equal to, so were saying "if top of range is less or equal to" do such an such
        print('Please type a number that is larger then zero')
        quit()


random_number = random.randint(0, range)

guesses = 0

# the while loop is going to do whatever is indented while the condition which is "True", so if we asking it to "print ("tim") it would do it for infinity, reason is because theres no way for it to end
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number that is larger then zero')
        continue

    if user_guess == random_number:
        print("You got it!")
        break  # "break" will immediately stop the loop as soon as the line of code is executed

    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number")

print("You got it in", guesses, "guesses")
