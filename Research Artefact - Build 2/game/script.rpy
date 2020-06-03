﻿# The script of the game goes in this file.

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
    e "The following code is asking for a translated recaptcha, if the user inputs the wrong recaptcha then it should return \"Incorrect answer, are you a robot?\". If the user inputs the correct recaptcha then it should return \"Correct answer, looks like you aren't a robot!\". Take a look at the following snippet of code carefully, see if you can figure out the issue."

    e "recaptchaInput = input(\"Enter this recaptcha below: 'R3C4pTchA'.\")
    \nif recaptchaInput in (\"Recaptcha\"\);
    \n___print[\"Correct answer, looks like you aren't a robot!\"]
    \nelif
    \n___print(\"Incorrect answer, are you a robot?\")"
    menu:

        # Incorrect answer
        "recaptchaInput = input(\"Enter this recaptcha below: 'R3C4pchTA'.\")
        \nif recaptchaInput in [\"Recaptcha\"\];
        \n___print(\"Incorrect answer, are you a robot?\")
        \nelif
        \n___print(\"Correct answer, access granted.\")":
            jump IncorrectAnswer

        # Incorrect answer
        "recaptchaInput = input(\"Enter this recaptcha below: 'R3C4pchTA'.\")
        \nif recaptchaInput in ('Recaptcha'\);
        \n___print[\"Correct answer, looks like you aren't a robot!\"]
        \nelif
        \n___print[\"Incorrect answer, are you a robot?\"]":
            jump IncorrectAnswer

        # Correct answer
        "recaptchaInput = input(\"Enter this recaptcha below: 'R3C4pchTA'.\")
        \nif recaptchaInput in [\"Recaptcha\"\];
        \n___print(\"Correct answer, access granted.\")
        \nelif
        \n___print(\"Incorrect answer, are you a robot?\")":
            jump CorrectAnswer

    label Question2:
            $ rightAnswer = "Correct answer2"
            $ wrongAnswer = "Incorrect answer2"

            #Question 2 here
            e "The following code is a similar exercise based around collections. The code is trying to display the name of the game and it's release date, it should be printing something like this:
            \n
            \nFallout 3 was released in 2008
            \n
            \nFallout 3, 2008
            \nFallout New Vegas, 2010
            \nFallout 4, 2015
            \n
            \nSee if you can figure out the problem with the following code snippet."

            e "games = \{
            \n___\"Fallout 3\": \"2008\",
            \n___\"Fallout New Vegas\": \"2010\",
            \n___\"Fallout 4\": \"2015\"
            \n
            \nfor game releaseDate in game.items\{\}:
            \n___print \"\%s\" \% games + \" was released in \" + \"\%s.\" \% ReleaseDate
            \n\}"

            menu:

                # Incorrect answer
                "games = \{
                \n___\"The Elder Scrolls: Morrowind\": \"2002\",
                \n___\"The Elder Scrolls: Oblivion\": \"2006\",
                \n___\"The Elder Scrolls: Skyrim\": \"2011\"
                \n\}
                \n
                \nfor game releaseDate in game.items\{\}:
                \n___print \{\"\%s\" \% games + \" was released in \" + \"\%s.\" \% releaseDate\}":
                    jump IncorrectAnswer

                # Correct answer
                "games = \{
                \n___\"Fallout 3\": \"2008\",
                \n___\"Fallout New Vegas\": \"2010\",
                \n___\"Fallout 4\": \"2015\"
                \n\}
                \n
                \nfor game, releaseDate in games.items\(\):
                \n___print \(\"\%s\" \% game + \" was released in \" + \"\%s.\" \% releaseDate\)":
                    jump CorrectAnswer

                # Incorrect answer
                "Games = \{
                \n___\"The Elder Scrolls: Morrowind\": 2002,
                \n___\"The Elder Scrolls: Oblivion\": 2006,
                \n___\"The Elder Scrolls: Skyrim\": 2011
                \n\}
                \n
                \nfor game releaseDate in game.items\{\}:
                \n___print \(\"\%s\" \% game + \" was released in \" + \"\%d.\" \% releaseDate\)":
                    jump IncorrectAnswer

    label Question3:
            $ rightAnswer = "Correct answer3"
            $ wrongAnswer = "Incorrect answer3"

            #Question 3
            e "The following exercise is a similar exercise based around branches. The following code is trying to create a variable representing the user's height and give a response to the user's input based on their height. See if you can find the errors within the code."

            e "height == int.input(\"How tall are you?'))
            \n
            \nif height <= 5'6
            \n___print (\'You're allowed to ride without an adult!\')
            \nelif height > 5' \& year < 5'5:
            \n___print (\"You're allowed to ride but must be accompanied by an adult!\")
            \nelif:
            \n___print (\"Sorry! You're too small to ride on this!\")"

            menu:

                # Incorrect answer
                "Height == int(input(\"How tall are you?\"))
                \n
                \nif height <= 5'6:
                \n___print (\"You're allowed to ride without an adult!\")
                \nelse year < 5' & year > 5'5:
                \n___print (\"You're allowed to ride but must be accompanied by an adult!\")
                \nelse:
                \n___print (\"Sorry! You're too small to ride on this!\")":
                    jump IncorrectAnswer

                # Incorrect answer
                "height = int.input(\"How tall are you?\"))
                \n
                \nif height >= (\"5'6\"):
                \n___print (\"You're allowed to ride without an adult!\")
                \nelif year < 5' and year > 5'5:
                \n___print (\"You're allowed to ride but must be accompanied by an adult!\")
                \nelse:
                \n___print (\"Sorry! You're too small to ride on this!\")":
                    jump IncorrectAnswer

                # Correct answer
                "height = int(input(\"How tall are you?\"))
                \n
                \nif height <= 5'6:
                \n___print (\"You're allowed to ride without an adult!\")
                \nelif year > 5' and year < 5'5:
                \n___print (\"You're allowed to ride but must be accompanied by an adult!\")
                \nelse:
                \n___print (\"Sorry! You're too small to ride on this!\")":
                    jump CorrectAnswer


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
