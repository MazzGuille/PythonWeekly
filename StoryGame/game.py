game = True
while game == True:
    print()
    print("Welcome to MazzCodes's adventure game! You will be presented with a series of choices.\n You will determine your fate by making the  right choices.\n let's see if you can make it out alive... Good luck!\n")
    print()
    print("You wake up inside a dark room. You can't see a thing.\n You hear a voice in your head.\n It says, 'You are going to die.\n You have to  make a choice.\n You can either go left or right.\n Which way do you go?'")
    print()
    answer1 = input("Enter LEFT or RIGHT: ")
    answer1 = answer1.upper()
    print()
    if(answer1 == "LEFT"):
        print("You go left and find a door.\n You open the door and see a light.\n You walk into the light.\n You see a dead body.\n It seems to    have a cell phone, do you pick it up?\n")
        answer2 = input("Enter YES or NO: ")
        answer2 = answer2.upper()
        if(answer2 == "YES"):
            print("You go for the cell phone and all of a sudden, the dead body isnt dead anymore...\n It grabs your arm with huge strngth and  tries to bite you.\n You take a quick look near you, there is a machete, an iron bar and a gun.\n what do you do?.\n")
            answer3 = input("Enter MACHETE, BAR, KICK or GUN: ")
            answer3 = answer3.upper()
            if(answer3 == "MACHETE"):
                print("You grab the machete and slice the attacker's arm out.\n")
            elif(answer3 == "BAR"):
                print("You grab the bar and hit the attacker with it.\nIt doesnt affect it at all, he bites you.\n You are dead...\nGAME OVER")
                print("Would you like to play again? (y/n)")
                playAgain = input("Enter y or n: ")
                playAgain = playAgain.upper()
                if(playAgain == "Y"):
                    game = True
                else:
                    print("Thanks for playing! Better luck next time!")
                    game = False
            elif(answer3 == "KICK"):
                print("You kick the attacker with all your strength.\nThe attacker now has your leg, it starts chewing it off, you are dead...\n    GAME OVER")
            elif(answer3 == "GUN"):
                print("You grab the gun and shoot the attacker.\n The gun has no bullets, the attacker jump's on you and bites your face, you are   dead...\n GAME OVER")
           
           
                
    
    elif(answer1 == "RIGHT"):
        print("You go right and find a some stairs.\n You notice you are on the 5th floor and a sign that reads: \"Next floor rooftop\"\nDo you go  up or down?\n")