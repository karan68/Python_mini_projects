import random
n = random.randint(0,100)
chances=6
print("you have only 6 chances best of luck")
for num in range (chances):
    u=int(input("guess my no:\t"))
    chances = chances - 1
    print("you have", (chances), "chances left")

    if u>n :
        print("you have entered a bigger no. try again")
        continue

    elif u<n:
        print("you have entered a smaller no. try again")
        continue
    elif u==n:
        print("you are right with the no. being: ", n)
        break

if chances == 0:
    print("Game Over")
    print("the no. was: ", n)



