import random
options = []
for all_numbers in range(1, 101):
    options.append(all_numbers)
picked_number = random.choice(options)
tries = 0
print(f"Welcome to the guessing number game. All the numbers from 1 to 100 are taking part in it. If you want to give up, type Give Up.\n")
while True:
    tries += 1
    number_of_player = input("Please enter a number from 1 to 100:\n")
    if number_of_player == "Give Up" or number_of_player == "give up" or number_of_player == "Give up" or number_of_player == "give Up":
        print(f"The right number is {picked_number}!")
        quit()
    number_of_player = int(number_of_player)
    if number_of_player < 1 or number_of_player > 100:
        print(f"That's not a number between 1 and 100\n")
        continue
    if picked_number < number_of_player:
        print(f"Your number is bigger then my number.\n")
        continue
    elif picked_number > number_of_player:
        print(f"Your number is smaller then my number\n")
        continue
    else:
        print(f"YES! {picked_number} is the number that I chose!")
        print(f"Tries - {tries}")
        quit()