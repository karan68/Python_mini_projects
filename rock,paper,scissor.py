from random import randint
print("welcomw to the rock,paper and scissor")
print("there will be 5 rounds hope you win!")
#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False
u=0
c=0

i=6
while player == False and i>0:
#set player to True
    player = input("Rock, Paper, Scissors?: \t")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            c+=1
        else:
            print("You win!", player, "smashes", computer)
            u+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            c+=1
        else:
            print("You win!", player, "covers", computer)
            u+=1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            c+=1
        else:
            print("You win!", player, "cut", computer)
            u+=1
    else:
        print("That's not a valid play. Check your spelling!")
    i-=1
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]
if u>c:
    print("congo you won the rounds")
elif u<c:
    print("computer takes the victory")
else:
    print("aghhhh! this is a tie")
print("computer:", c)
print("you:", u)

