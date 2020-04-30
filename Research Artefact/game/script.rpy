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
    e "Take a look at the following snippet of code carefully, see if you can figure out the issue."
    e "passwordInput = input(\"What is the password?\"
    \nif passwordInput in [\"Password123\");
    \n___print(\"Correct password, access granted.\")
    \nelif
    \nprint(\"Incorrect password, access denied.\"."
    menu:

        # Correct answer
        "passwordInput = input(\"What is the password?\"\)
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
        \nprint(\"Incorrect password, access denied.\"\)":
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
            e "Insert question 2"
            e "games = \{
            \n___\"The Elder Scrolls: Morrowind\": \"2002\",
            \n___\"The Elder Scrolls: Oblivion\": \"2006\",
            \n___\"The Elder Scrolls: Skyrim\": \"2011\"
            \n
            \nfor game releaseDate in game.items\{\}:
            \n___print \"\%s\" \% games + \" released in \" + \"\%s.\" \% ReleaseDate
            \n \}"

            menu:

                # Incorrect answer
                "Incorrect answer 2":
                    jump incorrectAnswer

                # Correct answer
                "games = \{
                \n___\"The Elder Scrolls: Morrowind\": \"2002\",
                \n___\"The Elder Scrolls: Oblivion\": \"2006\",
                \n___\"The Elder Scrolls: Skyrim\": \"2011\"
                \n\}
                \n
                \nfor game releaseDate in game.items\(\):
                \n___print \(\"\%s\" \% game + \" released in \" + \"\%s.\" \% releaseDate\)":
                    jump CorrectAnswer

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
