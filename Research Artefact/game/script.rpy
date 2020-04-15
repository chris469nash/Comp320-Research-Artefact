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

# Add strings for each

    label Question1:
    $ currentQuestion = 1
    $ rightAnswer = "Correct answer"
    $ wrongAnswer = "Incorrect answer"

    # Use \ with special characters to print them, and use \n to make a new line.
    # Question 1 here
    e "Insert debugging question here"
    menu:

        # Correct answer
        "Correct answer 1":
            jump CorrectAnswer

        # Incorrect answer
        "Incorrect answer 1":
            jump IncorrectAnswer

        # Incorrect answer
        "Incorrect answer 1":
            jump IncorrectAnswer

        # Incorrect answer
        "Incorrect answer 1":
            jump IncorrectAnswer

        # Incorrect answer
        "Incorrect answer 1":
            jump IncorrectAnswer

    label Question2:
            $ rightAnswer = "Correct answer2"
            $ wrongAnswer = "Incorrect answer2"

            #Question 2 here
            e "Insert question 2"

            menu:

                # Incorrect answer
                "Incorrect answer 2":
                    jump incorrectAnswer

                # Correct answer
                "Correct answer 2":
                    jump CorrectAnswer

                # Incorrect answer
                "Incorrect answer 2":
                    jump IncorrectAnswer

                # Incorrect answer
                "Incorrect answer 2":
                    jump IncorrectAnswer

                # Incorrect answer
                "Incorrect answer 2":
                    jump IncorrectAnswer

    label Question3:
            $ rightAnswer = "Correct answer3"
            $ wrongAnswer = "Incorrect answer3"

            #Question 3
            e "Insert question 3"

            menu:

                # Incorrect answer
                "Incorrect answer 3":
                    jump incorrectAnswer

                # Incorrect answer
                "Incorrect answer 3":
                    jump incorrectAnswer

                # Correct answer
                "Correct answer 3":
                    jump CorrectAnswer

                # Incorrect answer
                "Incorrect answer 3":
                    jump IncorrectAnswer

                # Incorrect answer
                "Incorrect answer 3":
                    jump IncorrectAnswer

    # Correct answer response
    label CorrectAnswer:

        e "[rightAnswer]"

        jump nextQuestion

    #Incorrect answer response
    label IncorrectAnswer:

        e "[wrongAnswer]"

        jump nextQuestion

# Jump to next question
    label nextQuestion:
        $ currentQuestion += 1
        if currentQuestion == 2:
            jump Question2

        if currentQuestion == 3:
            jump Question3
    return
