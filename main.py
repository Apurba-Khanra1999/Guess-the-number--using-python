import random

num = random.randint(1, 10)
for i in range(0,3):   # You will get three chances to guess the number
    enduser = int(input("Guess Number B/W 1 - 10 "))

    if enduser == num:
        print("Yep ! You guessed the correct number ")
        break
    if enduser != num:
        print("Sorry ! You guessed Wrong")
print(f"The correct number is {num}")     #for printing the correct number 