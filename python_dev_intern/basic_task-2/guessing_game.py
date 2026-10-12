import random

n = random.randint(1,100)
for _ in range(7):
    g = int(input("Guess: "))
    if g == n:
        print("Correct!")
        break
    print("Too high" if g > n else "Too low")
else:
    print("Game over. Number:", n)