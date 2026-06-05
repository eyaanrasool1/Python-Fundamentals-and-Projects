import random
computer =random.choice([1, -1, 0])
youstr = input("enter your choice:  ")
youdict = {"snake": 1, "water": -1, "gun": 0}
reversedict = {1:"snake", -1:"water", 0:"gun"}
you=youdict[youstr]

print(f"You choose {reversedict[you]},\nOther choose",reversedict[computer])

if(computer == you):
    print ("its Draw")
elif ((computer - you) == -1 or (computer-you) == 2):
    print ("you lose")
else:
    print("you win")

