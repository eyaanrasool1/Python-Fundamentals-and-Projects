import random

n = random.randint(1, 100)
a = -1
guesses = 0

while a != n:
    a = int(input("Enter the number: "))
    guesses += 1

    if a > n:
        print("Enter a lower number")
    elif a < n:
        print("Enter a higher number")

print(f"You got the number in {guesses} guesses. The number was {n}.")