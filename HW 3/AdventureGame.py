# ONE NIGHT IN THE HAUNTED MANSION

# An object describing our player
player = {
    "name": "p1"
}


def printGraphic(name):
    if (name == "title"):
        print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print (' ONE NIGHT IN THE HAUNTED MANSION')
        print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print ('                                 ')
        print ('      .````.      ...            ')
        print ('     :o  o `....``  ;            ')
        print ('     `. O         :`             ')
        print ('       ``:          `.           ')
        print ('         `:.          `.         ')
        print ('          : `.         `.        ')
        print ('         `..``...       `.       ')
        print ('                 `...     `.     ')
        print ('                     ``...  `.   ')
        print ('                          `````. ')
        print ('                                `')
    
    if (name == "dead"):
        print("   _                   _ ")
        print(" _( )                 ( )_ ")
        print("(_, |      __ __      | ,_) ")
        print("   \'\    /  ^  \    /'/ ")
        print("    '\'\,/\      \,/'/' ")
        print("      '\| []   [] |/' ")
        print("        (_  /^\  _) ")
        print("          \  ~  / ")
        print("          /HHHHH\ ")
        print("        /'/{^^^}\'\ ")
        print("    _,/'/'  ^^^  '\'\,_ ")
        print("   (_, |           | ,_) ")
        print("     (_)           (_) ")

    if (name == "winner"):
        print("------------------------------------")
        print("|#######====================#######|")
        print("|#(1)*UNITED STATES OF AMERICA*(1)#|")
        print("|#**          /===\   ********  **#|")
        print("|#           | (-) |             #*|")
        print("|#*  ******  | /v\ |    O N E    *#|")
        print("|#(1)         \===/            (1)#|")
        print("|##========= $1,000,000 =========##|")
        print("------------------------------------")



def introStory():
    # let's introduce them to our world
    print ("Hi, there. Who am I speaking with?")
    player["name"] = input("Please enter your name> ")
    print ("")

    print ( player["name"] + "," + " you've been noticed by the esteemed inventor, Martin Randall.")
    print ("A busy man with a lonely streak, Mr. Randall is looking to throw a party--or at least, what he calls a party...")
    print ("He cordially invites you to stay one night in his haunted mansion for a chance to win $1 million dollars.")
    print ("If you can make it through the night, the money is all yours.") 
    print ("")
    print ("Now, the question remains... do you accept?")

    pcmd = input("Choose: (1) Sign me up! OR (2) I, uh... can't make it...> ")
    print("")

    # the player can choose 1 or 2
    if (pcmd == "1"):
        path1()

    elif (pcmd == "2"):
        print ("No? Too late, Mr. Randall already sent a car. Hope you're fast a packer.")
        print(input("Press enter>"))
        path1()

    else: 
        path1()

def path1():
    print ("You arrive at the mansion, enter, and are greeted by the gatekeeper, Igor, who takes your belongings.")
    print ("'I was told to give you each one tool--should you need it to help get you through the night...,' mutters Igor as he reaches into his jacket. 'Let me see what I have for you...'")
    print (input("Press enter>"))

    import random
    myList = ["a Flashlight", "a Kitchen Knife", "Rope", "a Mysterious Potion"]
    print("You've been gifted: " + random.choice(myList) + "!" )
    print (input("Press enter>"))

    print("Igor introduces you to the other guests. You...")

    # the player chooses 1 or 2
    pcmd1 = input("(1) Try to form an alliance OR (2) Keep to yourself and explore the mansion>")

    print ("")

    if (pcmd1 == "1"):
        print("You meet a sweet school teacher who tells you she's here to try and win money for her struggling school.")
        print("You trust her and tell her you'd like to stick together.")
        print("She agrees, and you alternate between being on look out and taking naps.")
        print("You scare away 10 ghosts over the course of the night and meet Mr. Randall in the morning.")
        print(input("Press enter>"))

        printGraphic("winner")
        print("")
        print("CONGRATS!! You both win $1 million dollars!!")

    elif (pcmd1 == "2"):
        print("You're wandering around, hallway after hallway, and finally come across a door slightly ajar, with light pouring out of the cracks.")
        print("You approach quietly and peer inside through the crack.")
        print("You see a life-size voodoo doll of yourself in the center of the room with all of the other guests surrounding it about to make a move.")
        print("You scream and they all turn around.")
        print("Everything goes black.")
        print (input("Press enter>"))

        printGraphic("dead")
        print("YOU'RE DEAD!")
        print("It's about time you learned the value of teamwork!")


# main! most programs start with this.
def main():
    printGraphic("title") # call the function to print an image
    introStory() # start the intro

main() # this is the first thing that happens