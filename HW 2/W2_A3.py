# let the user know what's going on
print ("Welcome to MadLibs!")
print ("Answer the questions below to play.")
print ("-----------------------------------")

# variables containing all of your story info
adjective1 = input("Enter an adjective: ")
celebrityName1 = input("Name a funny celebrity: ")
location1 = input("Name a room in a house: ")
object1 = input("An object from your home: ")
sound1 = input("Name a sound a person can make [past tense]: ")
celebrityName2 = input("Name a celebrity you think is silly: ")

# this is the story. it is made up of strings and variables.
# the \ at the end of each line let's the computer know our string is a long one
# (a whole paragraph!) and we want to continue more code on the next line. 
# play close attention to the syntax!

story = "Scooby Doo and the Gang encountered a " + adjective1 + " ghost while investing " + celebrityName1 + "'s " + location1 + "." \
" Spooked by what they saw, the Gang ran the other way, bumping into a " + object1 + " which fell on the floor. The ghost was so frightened by the sound, it " + sound1 + ", making its cloak fall off." \
" To everyone's surprise it was actually " + celebrityName2 + "!" \


# finally we print the story
print (story)