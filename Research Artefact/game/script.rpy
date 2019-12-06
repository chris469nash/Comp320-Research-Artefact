# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "Welcome to my Comp320 Research Artefact Prototype"

    e "Please take your time to answer each question, your data from these results is crucial to my dissertation!"

    # Question 1:

    e "Insert debugging question here"

    menu:

        # Correct answer
        "Correct answer":
            jump correctq1

        # Incorrect answer
        "Incorrect answer 1":
            jump incorrectq1

        # Incorrect answer
        "Incorrect answer 2":
            jump incorrectq2

        # Incorrect answer
        "Incorrect answer 3":
            jump incorrectq3

        # Incorrect answer
        "Incorrect answer 4":
            jump incorrectq4

        # Correct answer response
    label correctq1:

        e "Well done!, you chose the correct answer!"

        return

        #Incorrect answer response
    label incorrectq1:

        e "Oh no! You chose the incorrect answer!"

        return

        #Incorrect answer response
    label incorrectq2:

        e "Oh no! You chose the incorrect answer!"

        return

        #Incorrect answer response
    label incorrectq3:

        e "Oh no! You chose the incorrect answer!"

        return

        #Incorrect answer response
    label incorrectq4:

        e "Oh no! You chose the incorrect answer!"

    # This ends the game.

    return
