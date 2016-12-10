from sys import exit


# define what happens when you die
def dead(why):
    # print the reason stated in the level and then a generic conclusion
    print why, "Unfortunately, you lose!"
    # exit the program
    exit(0)


# LEVEL 1

# beginning scene
def start():
    print "You wake up in the hollow of an oak tree... cold... disoriented."
    print "Sleep threatens to pull you into its depths again."
    print "What will you do?"
    print "\t1. Close your eyes, and allow your exhaustion to pull you under..."
    print "\t2. Sit up and look around."

    # creates a loop so that if user types in an unrecognized answer they can try again
    while True:
        # allows for input by the user
        choice = raw_input("> ")

        # user must type the number of the desired response to continue
        if choice == "1":
            dead("The darkness swallows you forever.")
        elif choice == "2":
            tree()
        # in case the user types something that is not a recognized number
        else:
            print "I don't understand what you are saying."

# next scene if option 2 in START is selected
def tree():
    # description of scene
    print "The forest is shadowy. Something rustles in the tree above your head."
    print "The landscape is unfamiliar, but it looks like there are a few paths winding away between the trees."
    print "What will you do?"
    print "\t1. Take the first path."
    print "\t2. Take the second path."
    print "\t3. Curl up and remain beneath the tree forever."

    # description of choices
    while True:
        choice = raw_input("> ")

        if choice == "1":
            path1()
        elif choice == "2":
            path2()
        elif choice == "3":
            dead("The darkness swallows you again.")
        else:
            print "I don't understand what you are saying."


# LEVEL 2

# next scene if option 1 in TREE is selected
def path1():
    # description of scene
    print "You arrive at a crossroads."
    print "To the left is a cluster of bushes that look like they may have berries."
    print "Your stomach rumbles."
    print "To the right you can hear the gentle babbling of a stream."
    print "Your throat is very parched."
    print "Where will you go?"
    print "\t1. To the bushes."
    print "\t2. To the river."
    print "\t3. Head off in another direction."

    # description of choices
    while True:
        choice = raw_input("> ")

        if choice == "1":
            bush()
        elif choice == "2":
            river()
        elif choice == "3":
            path2()
        else:
            print "I don't understand what you are saying."

# next scene if option 2 in TREE is selected
def path2():
    # description of scene
    print "You arrive at a crossroads."
    print "To the left you can see moonlight shining through the thinning trees."
    print "You suddenly ache for the touch of the light."
    print "To the right is a clearing. Looking up, you see that a wisp of smoke is curling above the trees."
    print "Perhaps there is a person there who can aid you."
    print "Where will you go?"
    print "\t1. To the moonlight."
    print "\t2. To the clearing."
    print "\t3. Head off in another direction."

    # description of choices
    while True:
        choice = raw_input("> ")

        if choice == "1":
            cliff()
        elif choice == "2":
            clearing()
        elif choice == "3":
            path1()
        else:
            print "I don't understand what you are saying."


# LEVEL 3

def bush():
    # description of scene
    print "You come across a cluster of fruit-bearing bushes."
    print "The fruit is small and round and deep purple in color."
    print "Your stomach rumbles. You're starving."
    print "Do you take some of the berries?"
    print "\t1. Eat all of the berries you can get your hands on."
    print "\t2. Take just a handful of berries."
    print "\t3. Don't eat any of the berries; you'll find food later."
    print "\t4. Turn around and go back to where you came from."
    print "\t5. Head in a different direction."

    # description of choices
    while True:
        choice = raw_input("> ")

        if choice == "1":
            dead("That's way too many berries! They make you sick.")
        elif choice == "2":
            print "The berries are sweet and stain your fingers a vibrant red-purple. The food has revived you."
            earth()
        elif choice == "3":
            dead("You're so hungry, you don't think you'll make it.")
        # takes you back to the path if you want a different choice
        elif choice == "4":
            path1()
        # takes you directly to the other choice in PATH1
        elif choice == "5":
            river()
        else:
            print "I don't understand what you are saying."

def river():
    # description of scene
    print "You come across a brook winding through the trees."
    print "The water is very clear and inviting."
    print "Your throat is parched. You're so thirsty."
    print "Do you drink from the stream?"
    print "\t1. Don't drink from it. Something about the shimmer of the water is disconcerting."
    print "\t2. Drink from it. Just a taste won't hurt."
    print "\t3. Turn around and go back to where you came from."
    print "\t4. Head in a different direction."

    # description of choices
    while True:
        choice = raw_input("> ")

        if choice == "1":
            dead("But you're so thirsty...")
        elif choice == "2":
            print "You cup the water in your hands and drink. The water is wonderfully cool. It revives you."
            water()
        # takes you back to the path if you want a different choice
        elif choice == "3":
            path1()
        # takes you directly to the other choice in PATH1
        elif choice == "4":
            bush()
        else:
            print "I don't understand what you are saying."

def cliff():
    # description of scene
    print "You emerge from the forest and into the moonlight."
    print "You are at a cliff's edge. Nervous, you linger by the treeline."
    print "Maybe you can get a sense of where you are if you walk out just a little farther."
    print "What will you do?"
    print "\t1. Walk out to inspect your surroundings."
    print "\t2. Head back into the forest the way you came."
    print "\t3. Head in a different direction."

    # description of choices
    while True:
        choice = raw_input("> ")

        if choice == "1":
            print "You step out into the moonlight and the fresh, clean air."
            air()
        elif choice == "2":
            path2()
        elif choice == "3":
            clearing()
        else:
            print "I don't understand what you are saying."

def clearing():
    # description of scene
    print "You approach the clearing, lingering at the edge of the forest."
    print "There's nothing there except the smoldering remains of a fire."
    print "You shiver. You're so cold. Maybe the embers will warm you."
    print "What will you do?"
    print "\t1. Warm yourself at the fire. There's no one around."
    print "\t2. Head back into the forest the way you came."
    print "\t3. Head in a different direction."

    # description of choices
    while True:
        choice = raw_input("> ")

        if choice == "1":
            print "You walk over to the fire and allow it to warm your hands."
            fire()
        elif choice == "2":
            path2()
        elif choice == "3":
            cliff()
        else:
            print "I don't understand what you are saying."


# LEVEL 4

def earth():
    # description of scene
    print "Your hands are tingling a little, and you feel energy coursing through you."
    print "There must have been something weird about those berries."
    print "Suddenly, there is a rustling from behind you. A bear emerges from the trees."
    print "Your heart stops as the bear levels its gaze at you, but your hands feel ready with energy."
    print "What will you do?"
    print "\t1. Run! Maybe you can make it out of there before the bear attacks."
    print "\t2. Stand your ground. You feel braver than you ever have before."

    # description of choices
    while True:
        choice = raw_input("> ")

        if choice == "1":
            dead("The bear chases after you! No matter how fast your legs carry you, you can't outrun him.")
        elif choice == "2":
            earth2()
        else:
            print "I don't understand what you are saying."

def water():
    # description of scene
    print "Your hands are tingling a little, and you feel energy coursing through you."
    print "But the rocks are slippery, and the stream runs deeper and faster than you first observed."
    print "Suddenly, you slip off-balance and fall into the water."
    print "The coldness of the water shocks all of the air out of your lungs."
    print "What will you do?"
    print "\t1. Wave your arms and try to right yourself."
    print "\t2. Allow yourself to be swept away. Maybe something better will happen down-river."

    # description of choices
    while True:
        choice = raw_input("> ")

        if choice == "1":
            water2()
        elif choice == "2":
            dead("You can't tell which way is up or down, and your lungs are slowly running out of air...")
        else:
            print "I don't understand what you are saying."

def air():
    # description of scene
    print "Your hands are tingling a little, and you feel energy coursing through you."
    print "You get lost staring up at the full moon, reveling in its beauty."
    print "Suddenly, there's a loud noise in the woods behind you. Startled, you jump a little."
    print "Unfortunately, your foot dips over the edge of the cliffside, and you lose your balance."
    print "Before you even know it, you are falling."
    print "What will you do?"
    print "\t1. Pray for a soft landing."
    print "\t2. Your palms are tingling; spread your arms and see if something will happen."

    # description of choices
    while True:
        choice = raw_input("> ")

        if choice == "1":
            dead("The landing is much less softer than you expected.")
        elif choice == "2":
            air2()
        else:
            print "I don't understand what you are saying."

def fire():
    # description of scene
    print "Your hands are tingling a little, and you feel energy coursing through you."
    print "Suddenly, there's a rustling from behind you."
    print "A man steps out into the clearing, weapon drawn."
    print "You straighten and stare him down, but your heart is pounding."
    print "What will you do?"
    print "\t1. Run! Maybe you can evade capture if you move fast enough."
    print "\t2. Stand your ground. You feel braver than you ever have before."

    # description of choices
    while True:
        choice = raw_input("> ")

        if choice == "1":
            dead("You are fast, but the man is faster.")
        elif choice == "2":
            fire2()
        else:
            print "I don't understand what you are saying."


# LEVEL 5

def earth2():
    # description of scene
    print "Your hands feel a magic they have never felt before."
    print "The bushes begin to bend and grow behind you, arching over your head."
    print "The bear, afraid, turns and runs from you."
    print "You use your newfound powers to create a shelter."
    print "In the daylight, you will be able to return home and extract your revenge."
    # moves automatically to the next scene without user input
    hilltop()

def water2():
    # description of scene
    print "Your hands feel a magic they have never felt before."
    print "The first movement of your arms sends you spinning out of the water."
    print "The stream swells and ebbs with the movement of your hands."
    print "You use your newfound powers to dry the water from your body and then seek shelter by the stream."
    print "In the daylight, you will be able to return home and extract your revenge."
    hilltop()

def air2():
    # description of scene
    print "Your hands feel a magic they have never felt before."
    print "Just by moving your arms, you are propelled upright in the air."
    print "You are no longer falling, but floating."
    print "You use your newfound powers to navigate back to the cliffside and sigh with relief when your feet touch earth again."
    print "You seek shelter at the edge of the forest."
    print "In the daylight, you will be able to return home and extract your revenge."
    hilltop()

def fire2():
    # description of scene
    print "Your hands feel a magic they have never felt before."
    print "You wave your fingers, and the fire springs to life behind you and follows the movement of your arms."
    print "The man shrieks and flees in terror."
    print "You use your newfound powers to keep the fire going."
    print "In the daylight, you will be able to return home and extract your revenge."
    hilltop()


# LEVEL 6

def hilltop():
    # description of scene
    print "\nIn the daylight, you can navigate effortlessly through the forest."
    print "Though maybe that's the effect of your new powers."
    print "You alight upon the hilltop that overlooks the home of your old family."
    print "What will you do?"
    print "\t1. Use your new powers to extract revenge on your relatives that exiled you. \n\tThey deserve what's coming to them."
    print "\t2. Turn away and live in the forest in solitude. \n\tThey do not deserve the same pain they inflicted on you."

    # description of choices
    while True:
        choice = raw_input("> ")

        if choice == "1":
            print "Your relatives cower in fear at your nature-given powers. They will not dare to cross you again."
            print "In your own sort of way, you have won."
            # the game has been won, so the program terminates
            exit(0)
        elif choice == "2":
            print "You spend the rest of your days in the forest, haunting travelers and conversing with the birds."
            print "In your own sort of way, you have won."
            # the game has been won, so the program terminates
            exit(0)
        else:
            print "I don't understand what you are saying."


start()
