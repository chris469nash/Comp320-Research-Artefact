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
    e "The following code is asking for a password, if the user inputs the wrong password then it should return, \"Incorrect password, access denied.\". If the user inputs the correct password then it should return \"Correct password, access granted.\". Take a look at the following snippet of code carefully, see if you can figure out the issue."

    e "passwordInput = input(\"What is the password?\"
    \nif passwordInput in [\"Password123\");
    \n___print(\"Correct password, access granted.\")
    \nelif
    \nprint(\"Incorrect password, access denied.\"."

    menu:

        # Correct answer
        "passwordInput = input(\"What is the password?\")
        \nif passwordInput in [\"Password123\"\];
        \n___print(\"Correct password, access granted.\")
        \nelif
        \n___print(\"Incorrect password, access denied.\")":
            jump CorrectAnswer

        # Incorrect answer
        "passwordInput = input(\"What is the password?\"
        \nif passwordInput in [\"Password123\");
        \nprint(\"Correct password, access granted.\")
        \nelif
        \nprint(\"Incorrect password, access denied.\")":
            jump IncorrectAnswer

        # Incorrect answer
        "passwordInput = input(\"What is the password?\"if passwordInput in [\"Password123\");
        \n___print(\"Correct password, access granted.\")
        \nelif
        \n___print(\"Incorrect password, access denied.\"\)":
            jump IncorrectAnswer

    label Question2:
            $ rightAnswer = "Correct answer2"
            $ wrongAnswer = "Incorrect answer2"

            #Question 2 here
            e "The following code exercise is based around collections. The code is trying to display the name of the game and it's release date, it should be printing something like this:
            \n
            \nThe Elder Scrolls: Morrowind was released in 2002
            \n
            \nThe Elder Scrolls: Morrowind, 2002
            \nThe Elder Scrolls: Oblivion, 2006
            \nThe Elder Scrolls: Skyrim, 2011
            \n
            \nSee if you can figure out the problem with the following code snippet."

            e "games = \{
            \n___\"The Elder Scrolls: Morrowind\": \"2002\",
            \n___\"The Elder Scrolls: Oblivion\": \"2006\",
            \n___\"The Elder Scrolls: Skyrim\": \"2011\"
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
                \n___\"The Elder Scrolls: Morrowind\": \"2002\",
                \n___\"The Elder Scrolls: Oblivion\": \"2006\",
                \n___\"The Elder Scrolls: Skyrim\": \"2011\"
                \n\}
                \n
                \nfor game, releaseDate in games.items(\):
                \n___print \(\"\%s\" \% game + \" was released in \" + \"\%s.\" \% releaseDate\)":
                    jump CorrectAnswer

                # Incorrect answer
                "gams = \{
                \n___\"The Elder Scrolls: Morrowind\": \"2002\",
                \n___\"The Elder Scrolls: Oblivion\": \"2006\",
                \n___\"The Elder Scrolls: Skyrim\": \"2011\"
                \n\}
                \n
                \nfor game releaseDate in game.items\{\}:
                \n___print \(\"\%s\" \% game + \" was released in \" + \"\%d.\" \% releaseDate\)":
                    jump IncorrectAnswer

    label Question3:
            $ rightAnswer = "Correct answer3"
            $ wrongAnswer = "Incorrect answer3"

            #Question 3
            e "The following exercise is based around branches. The following code is trying to create a variable representing the user's age and give a response to the user's input based on their age. See if you can find the errors within the code."

            e "year == int.input(\"What year were you born in?'))
            \n
            \nif year <= 2000
            \n___print (\'You must be above the age of 20!\')
            \nelif year > 2010 \& year < 2020:
            \n___print (\"You must be above the age of 10!\")
            \nelif:
            \n___print (\"You must be below the age of 10!\")"

            menu:

                # Incorrect answer
                "year = int.input(\"What year were you born in?\"))
                \n
                \nif year >= (\"2000\"):
                \n___print (\"You must be above the age of 20!\")
                \nelif year < 2010 and year > 2020:
                \n___print (\"You must be above the age of 10!\")
                \nelse:
                \n___print (\"You must be below the age of 10!\")":
                    jump IncorrectAnswer

                # Correct answer
                "year = int(input(\"What year were you born in?\"))
                \n
                \nif year <= 2000:
                \n___print (\"You must be above the age of 20!\")
                \nelif year > 2010 and year < 2020:
                \n___print (\"You must be above the age of 10!\")
                \nelse:
                \n___print (\"You must be below the age of 10!\")":
                    jump CorrectAnswer

                # Incorrect answer
                "year == int(input(\"What year were you born in?\"))
                \n
                \nif year <= 2000:
                \n___print (\"You must be above the age of 20!\")
                \nelse year < 2010 and year > 2020:
                \n___print (\"You must be above the age of 10!\")
                \nelse:
                \n___print (\"You must be below the age of 10!\")":
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
