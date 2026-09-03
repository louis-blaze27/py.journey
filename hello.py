# This program says hello and then asks you a few questions about yourself. It then responds to your answers.

print('Hello World')
print('Booting .................................................................')
print()

print('What is your name?')                                                              # Ask for their Name.
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print()

print('What is your age?')                                                               # Ask for their Age.
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
print()

print('Quick fire round! Answer honestly...')
print()

print('Pineapple on pizza: yes or no?')                                                  # Ask for their opinion on pineapple on pizza.
pizza = input()
if pizza.lower() == 'yes':
    print('Bold choice. Respect.')
else:
    print('A purist. I like it.')
print()

print('Cats or dogs?')                                                                   # Ask for their preference between cats or dogs.
pet = input()
print('Ah, a ' + pet.lower() + ' person. Noted.')
print()

print('If you were a superhero, what would your power be?')                              # Ask for their superhero power.
power = input()
print(myName + ' the ' + power.title() + '! Has a nice ring to it.')
print()

print('On a scale of 1 to 10, how much do you like Python so far?')                      # Ask how they would rate Python.
rating = input()
if int(rating) >= 8:
    print("That's the spirit! Keep going, " + myName + '.')
else:
    print("Fair enough, it gets more fun the more you build!")
print()

print('Last one: what is your favorite food?')                                           # Ask for their favorite food.
food = input()
print('Mmm, ' + food + '. Great taste.')
print()

print('Thanks for chatting, ' + myName + '! See you in the next program.')
