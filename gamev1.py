from sys import exit

def bush():
    print "You come across a bush that looks like it has some fruit on it."
    print "Do you take some?"
    print "\t1. Take a handful of berries."
    print "\t2. Eat all the berries on the bush."
    print "\t3. Don't eat any of the berries."

    choice = raw_input("> ")
    if choice == "1":
        print "The berries revived you."
        print "Congrats! You will live to make it out of the forest."
        exit(0)
    elif choice == "2":
        dead("That's way too many berries! They make you sick.")
    elif choice == "3":
        dead("You're so hungry, you don't think you'll make it.")
    else:
        print "I don't understand what you're saying."

def creek():
    print "You arrive at a creek flowing between the trees."
    print "You are so thirsty. Do you drink from it?"
    print "\t1. Don't drink from it. What if it's poisoned?"
    print "\t2. Go ahead, drink. What's the worst that could happen?"

    choice = raw_input("> ")
    if choice == "1":
        dead("But you're so thirsty...")
    if choice == "2":
        print "The water is cool and crystal clear. It revives you."
        print "Congrats! You will live to make it out of the forest."
        exit(0)

def dead(why):
    print why, "Unfortunately, you lose!"
    exit(0)

def start():
    print "You wake up in the hollow of a tree. Cold... Disoriented..."
    print "Where are you? You sit up and look around."
    print "The wood looks unfamiliar. What should you do?"
    print "\t1. Venture to the left."
    print "\t2. Venture to the right."
    print "\t3. Curl up and remain there forever."

    choice = raw_input("> ")

    if choice == "1":
        bush()
    elif choice == "2":
        creek()
    elif choice == "3":
        dead("The darkness swallows you again.")
    else:
        print "I don't understand what you're saying."

start()
