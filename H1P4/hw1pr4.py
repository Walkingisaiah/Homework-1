# coding: utf-8
#
# hw1pr4.py
#I worked alone

""" 
Title for your adventure:   The Quest.

Notes on how to "win" or "lose" this adventure:
  To win, choose the table.
  To lose, choose the door.

"""

import time

def adventure():
    """ this function runs one session of interactive fiction
        Well, it's "fiction," depending on the pill color chosen...
        arguments: no arguments (prompted text doesn't count as an argument)
        results: no results     (printing doesn't count as a result)
    """
    delay = 0.0          # change to 0.0 for testing or speed runs,
                         # ..larger for dramatic effect!

    username = input("What do they call you, worthy adventurer? ")

    print()
    print("Welcome,", username, " to the Libra Complex, a labyrinth")
    print("of weighty wonders and unreal quantities...of poptarts!")
    print()

    print("Your quest: To find--and partake of--a poptart!")
    print()
    flavor = input("What flavor do you seek? ")
    if flavor == "strawberry":
        print("Wise! You show deep poptart experience.")
    elif flavor == "s'mores":
        print("The taste of the campfire: well chosen, adventurer!")
    else:
        print("Each to their own, then.")
    print()

    print("On to the quest!\n\n")
    print("A corridor stretches before you; its dim lighting betrays, to one side,")
    print("a table supporting nameless forms of inorganic bulk and, to the other,")
    print("a door ajar, leaking laughter--is that laughter?--of lab-goers.")
    time.sleep(delay)
    print()

    choice1 = input("Do you choose the table or the door? [table/door/inside car] ")
    print()

    if choice1 == "table":
        print("As you approach the table, its hazy burdens loom ever larger, until...")
        time.sleep(delay)
        print("...they resolve into unending stacks of poptarts, foil shimmering.")
        print("You succeed, sumptuously, in sating the challenge--and your hunger.")
        print("Go well,", username, "!")
    elif choice1 == 'inside car':
        print("You have succeded but at what cost?......")
        print("You have found a half eaten", flavor, "poptart!")
        print("You decide to eat it but 30 minutes later you start taking poison damage!")
    else:  
        print("You push the door into a gathering of sagefowl, athenas, and stags alike,")
        print("all relishing their tasks. Teamwork and merriment abound here, except...")
        time.sleep(delay)
        print("...they have consumed ALL of the poptarts! Drifts of wrappers coat the floor.")
        print("Dizzy, you grasp for a pastry. None is at hand. You exhale and slip")
        print("under the teeming tide of foil as it finishes winding around you.")
        print("Farewell,", username, ".")
    print ("You have now encountered a serious problem: What will you have for lunch? (chips/sandwich/pizza) ")
    choice = input("What will your choice be? ")
    if choice == 'chips':
        print('Great choice... fast and tasty')
    elif choice == 'sandwich':
        print("Great choice, ", username, "....Healthy, fast, and filling!")
    elif choice == 'pizza': 
        print("Not bad... just be careful this could cause health issues but still very yummy")
    else:
        print('wrong answer.... ')
        print('You suddenly explode!')
    print ("Now you have another problem how will you get to work after all this food? car/helicopter")
    travel = input("Means of travel?")
    if travel == 'car':
        print("Great choice!... your car was not too far away and you save money")
    else:
        print("Terrible decision.....")
        print('There was suddenly a flash of light and you explode with enough force to wipe out half the nation')
    print("The next day comes along: suddenly you are in space and you cannot breath but you see two thing floating in the distance that can help you spacesuit/hotdog")
    space = input("What will your choice be?")
    if space == 'hotdog':
        print ("Congratulations! you have been saved... You throw hotdog to get momentum to return to earth safely")
    elif space =='spacesuit':
        print("Wrong answer... you are now floating in space with space suit but are stuck because you didn't choose hotdog :( ")
    print("Did you like my game Dave?")
    answer = input("Choose (yes or no): ")
    if answer == 'no':
        print('You suddenly explode with such devastating power... people in the ISS could see the destruction you have caused and are thinking to themselves that they now have nowhere to return home to')