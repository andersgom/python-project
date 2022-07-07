#USE time PACKAGE!!!!

import time

mynumbers = [i for i in range(100000)]

start_time = time.time()

mylist = []
[i**2 for i in mynumbers]

end_time = time.time()



def fire():
    print("OH NO! There's fire everywhere! What should you do?")
    print("Behind the couch there's a water spray, a fan, a fire extinguisher, and a Molotov cocktail.")

    start_time = time.time()


    answer = input("Choose your weapon to extinguish the fire! ")
    

    for i in range(2):
        if (i <= 2):
            if answer.lower() == "fire extinguisher":
                print("You did it! Now you can explore the room.")
                end_time = time.time()
                print("You took ",end_time-start_time, "seconds.")
                break
            elif answer.lower() == "molotov cocktail":
                print("Wow... You made it worse. GAME OVER.")
                break
            elif (answer.lower() == "water spray") | (answer.lower() == "fan"):
                print("No, you can't extinguish a fire with this. Try again.")
                answer = input()
            else:
                print("I don't understand what you're saying. Come again? ")
                answer = input()
        else:
            continue
    print("You couldn't extinguish the fire. GAME OVER.")
            


fire()