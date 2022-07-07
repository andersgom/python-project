import time

def fire():
    print("OH NO! There's fire everywhere! What should you do?")
    print("Behind the couch there's a water spray, a fan, a fire extinguisher, and a Molotov cocktail.")

    start_time = time.time()
    
    counter = 0
    while counter <= 2:
        answer = input("Choose your weapon to extinguish the fire! ")

        #if (i <= 2):
        if answer.lower() == "fire extinguisher":
            print("You did it! Now you can explore the room.")
            end_time = time.time()
            print("You took ",round(end_time-start_time), "seconds.")
            break
        elif answer.lower() == "molotov cocktail":
            print("Wow... You made it worse. GAME OVER.")
            break
        elif (answer.lower() == "water spray") | (answer.lower() == "fan"):
            print("No, you can't extinguish a fire with this. Try again.")
            counter +=1
        else:
            print("I don't understand what you're saying. Come again? ")
            counter +=1

    if counter  > 2 :
        print("You couldn't extinguish the fire. GAME OVER.")
    else:
        print('IM HERE')

        


fire()