import sys

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
        print("You go left and find a door.\n You open the door and see a light.\n You walk into the light.\n You see a dead body.\n It seems to have a cell phone, do you pick it up?\n")
        answer2 = input("Enter YES or NO: ")
        answer2 = answer2.upper()
        if(answer2 == "YES"):
            print("You go for the cell phone and all of a sudden, the dead body isnt dead anymore...\n It grabs your arm with huge strngth and  tries to bite you.\n You take a quick look near you, there is a machete, an iron bar and a gun.\n what do you do?.\n")
            answer3 = input("Enter MACHETE, BAR, KICK or GUN: ")
            answer3 = answer3.upper()
            if(answer3 == "MACHETE"):
                print("You grab the machete and slice the attacker's arm out.\n You reach a two way hallway.\n You can either go left or right.\n Which way do you go?")
                print()
                answer4 = input("Enter LEFT or RIGHT: ")
                answer4 = answer4.upper()
                if(answer4 == "LEFT"):
                    print("You go left, suddenly, you hear a roar, an enormus zombie dog jumps through a window from your right, he bites you in the neck, you are dead.\n GAME OVER")
                    print("Would you like to play again? (y/n)")
                    playAgain = input("Enter y or n: ")
                    playAgain = playAgain.upper()
                    if(playAgain == "Y"):
                        game = True
                    else:
                        print("Thanks for playing! Better luck next time!")
                        game = False
                        sys.exit()
                        
                elif (answer4 == "RIGHT"):
                    print("You go right, you see an exit sign, you find a door leading to the street.\n once outside, you see a newspaper, you check it out.\n The headline reads \"Zombie apocalypse!\"\nYou ntice the date and realize it's been 3 months since the last thing you can remember... Welcome to the beginig of the end...")
                    print("Congratulations, you finished the game!\n Thanks for playing!")
                    print("Would you like to play again? (y/n)")
                    playAgain = input("Enter y or n: ")
                    playAgain = playAgain.upper()
                    if(playAgain == "Y"):
                        game = True
                    else:
                        print("Thanks for playing! Better luck next time!")
                        game = False
                        sys.exit()
                    
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
                    sys.exit()
            elif(answer3 == "KICK"):
                print("You kick the attacker with all your strength.\nThe attacker now has your leg, it starts chewing it off, you are dead...\n    GAME OVER")
                print("Would you like to play again? (y/n)")
                playAgain = input("Enter y or n: ")
                playAgain = playAgain.upper()
                if(playAgain == "Y"):
                    game = True
                else:
                    print("Thanks for playing! Better luck next time!")
                    game = False
                    sys.exit()
            elif(answer3 == "GUN"):
                print("You grab the gun and shoot the attacker.\n The gun has no bullets, the attacker jump's on you and bites your face, you are   dead...\n GAME OVER")
                print("Would you like to play again? (y/n)")
                playAgain = input("Enter y or n: ")
                playAgain = playAgain.upper()
                if(playAgain == "Y"):
                    game = True
                else:
                    print("Thanks for playing! Better luck next time!")
                    game = False
                    sys.exit()
        elif(answer2 == "NO"):
            print("You turn your back to the dead body, the dead body stands up and attacks you from behind, he bites your neck, you are dead...\n GAME OVER")
            print("Would you like to play again? (y/n)")
            playAgain = input("Enter y or n: ")
            playAgain = playAgain.upper()
            if(playAgain == "Y"):
                game = True
            else:
                print("Thanks for playing! Better luck next time!")
                game = False
                sys.exit()           
           
                
    
    elif(answer1 == "RIGHT"):
        print("You go right and find a some stairs.\n You notice you are on the 5th floor and a sign that reads: \"Next floor rooftop\"\nDo you go  up or down?\n")
        answer5 = input("Enter UP or DOWN:")
        answer5 = answer5.upper()
        if(answer5 == "DOWN"):
            print("You start going down the stairs.\nYou see what seems to be a rat, the rat notices your there\nIt sqeeks loudly and dozens of rats come out of nowhere.\nYour sorrounded, the start jumping on you and biting you all over.\nYou are dead...\n GAME OVER")
            print("Would you like to play again? (y/n)")
            playAgain = input("Enter y or n: ")
            playAgain = playAgain.upper()
            if(playAgain == "Y"):
                game = True
            else:
                print("Thanks for playing! Better luck next time!")
                game = False
                sys.exit()
        elif(answer5 == "UP"):
            print("You reach the rooftop, you look down and see the city completely destroyed, no one on the streets\nYou try to take a better look around and find a newspaper, the headline reads \"Zombie apocalypse!\"\nYou notice the date and realize it's been 3 months since the last thing you can remember...\nOut of nowhere, a zombie bird attacks you, you trip and fall from the roof\nYou are dead...\n GAME OVER")
            print("Would you like to play again? (y/n)")
            playAgain = input("Enter y or n: ")
            playAgain = playAgain.upper()
            if(playAgain == "Y"):
                game = True
            else:
                print("Thanks for playing! Better luck next time!")
                game = False
                sys.exit()