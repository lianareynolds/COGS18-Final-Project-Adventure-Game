def play_game():

    """begins narrative by asking the user if they want to play,
    looping through the optional responses (Y/N) and calling 
    the next function (first_choice) to take them to the next diversion 
    in the game path, requesting input again 
    if they do not enter Y or N"""

    answer = ""

    while answer != "Y" and answer != "N":
        answer = input("Would you like to go on an adventure to another dimension? Y or N\n")
        if answer == "Y":
            print("Wonderful.")
            first_choice() #calls the function to send them to space
        elif answer == "N":
            print("Lame. Oh, well. Have a great day! :)")
            return #breaks the loop and ends the game immediately
        else:
            print("Oops, that wasn't Y or N")

def first_choice():

    """continues narrative by giving first choice in their space adventure
    through the use of if, elif, and else, calling the next function in the 
    narrative or calling the function that will send them back to the beginning"""

    run = 1

    while run:
        choice = input("Are you going 1)with inter-dimensional baddies or 2)alone?\
        Choose 1 or 2\n")
        if choice == "1":
            print("You blast off to explore endless galaxies in your rocketship")
            print("to go find another dimension where mortality doesn't exist.")
            space_adventure() #function that gives user the next obstacle to input
            break; 
        elif choice == "2":
            print("No no no...never go on an adventure alone. \
            You'll get lonely. And die.")
            restart() #user dies, restart() asks if they would like to try again
            break;
        else:
            print("Okay, I get it. You don't like following rules.")
            print("That's why you're on this adventure!")
            print("But I'm going to need a 1 or a 2 to go forward.")

def space_adventure():

    """continues adventure in space where first obstacle is prompted,
    either calling the next function in the narrative or sending the 
    user back to the beginning."""

    go = 1

    while go:
        obstacle = input("You encounter a band of inter-dimensional pirates!\
        Do you want to 1) fight or 2) run?\n")
        if obstacle == "1":
            print("You have courage in your veins!")
            print("Good thing you're a world class fencer back on old bluey earth")
            print("The captain came at you with rage and tyranny")
            print("but you were fiercer in justice and wisdom!")
            print("While you don't endorse killing,")
            print("it had to be done to save the lives of your fellow astronauts.")
            print("As you continue on your way paving a path through the universe")
            print("you get sucked into a wormhole and spat out in another dimension")
            dimension() #calls function giving user the next input in the adventure
            break
        elif obstacle == "2":
            print("Well, you escaped the fearsome pirates,")
            print("but you got off course and ran out of fuel.")
            print("Now you're stranded, and the food supplies are running low...")
            print("To prevent a Donner party situation,")
            print("you all decide to leap into space and float to your demise.")
            restart()
            break
        else:
             print("You can't escape fate...choose 1 or 2")

def dimension():

    """continues narrative to second obstacle in another dimension, this time
    either ending the game with a win and an option to play again (restart()) or 
    dying and an option to begin again (restart())"""

    new_dimension = ""

    # keep going until dimension is 1 or 2
    while new_dimension != "1" and new_dimension != "2":
        print("AWE would be an understatement for your reaction")
        print("This new dimension...it's unlike anything you've seen")
        print("It's vibrant and plentiful...")
        print("It looks like old bluey earth before humans destroyed it")
        new_dimension = input("Do you 1) stay here and risk destroying it or\
        2) leave to go find another dimension?")
        if new_dimension == "1":
            print("You live out the rest of your days in this dimension")
            print("of beauty and serenity.")
            print("You lead a society that doesn't make the same mistakes")
            print("as our's did. You made the right choice.")
            restart()
        elif new_dimension == "2":
            print("Look, you tried to do the right thing.")
            print("As it turns out, what you thought was the right thing")
            print("was just fear and cowardice.")
            print("I'm sorry to have to tell you this...")
            print("but in trying to escape the black hole, you were disintegrated.")
            restart()
        else:
            print("Please, you're giving me a headache. 1 or 2 only.")

def restart():

    """restart acts as an option to begin the game again by sending user back
    to the beginning of the code where they will be asked whether they want to go on
    an adventure again"""

    again = ""

    while again != "Y" and again != "N":
        again = input("Would you like to adventure again?\
        Your probability of dying will be low! Choose Y or N\n")
        if again == "Y":
            play_game() #sends user back to the beginning to restart
        elif again == "N":
            print("That's too bad. We'll miss you on our adventures!")
            print("Good luck in life, dear friend.")
        else:
            print("Don't you get the rules by now? It has to be Y or N")

#execute function
#play_game()
