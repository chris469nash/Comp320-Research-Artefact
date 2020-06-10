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
    $ rightAnswer = "Well done! You got this exercise correct!"
    $ wrongAnswer = "Oh no! You got this exercise incorrect!\n \nOption 1 had the responses in an incorrect order, the first print string should have returned \"Correct answer, looks like you aren't a robot!\" and the second print string should have returned \"Incorrect answer, are you a robot?\" \n \nOption 2 contained the inccorect use of '[' and ']' for a print string, they should be using '(' and ')'."

    # Use \ with special characters to print them, and use \n to make a new line.

    e "Take a look at this quick video, it will assist you in the upcoming question."

    $ renpy.movie_cutscene("Dramatic.webm")

    e "If you missed any part of the video, please click the 'Back' button located at the bottom left of the screen."
    #Question 1 here
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
            $ rightAnswer = "Well done! You got this exercise correct!"
            $ wrongAnswer = "Oh no! You got this exercise incorrect! \n \nOption 1 had syntax errors that made use of curly braces instead of using '(' and ')' to input the string and after the 'game.items'! \n \nOption 3 also had syntax errors, naming conventions weren't consistent throughout!"

            e "Take a look at this quick video, it will assist you in the upcoming question."

            $ renpy.movie_cutscene("Dramatic.webm")

            e "If you missed any part of the video, please click the 'Back' button located at the bottom left of the screen."
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
                \nfor game ReleaseDate in game.items\(\):
                \n___print \(\"\%s\" \% game + \" was released in \" + \"\%d.\" \% releaseDate\)":
                    jump IncorrectAnswer

    label Question3:
            $ rightAnswer = "Well done! You got this exercise correct! \n \nThank you for participating within this study! If you would like to read the dissertation that is connected to this research artefact then please send an email expressing interest in this to CN196703@falmouth.ac.uk and I will send you a copy once completed!"
            $ wrongAnswer = "Oh no! You got this exercise incorrect! \n \nOption 1 has its print strings in the wrong order, whilst this code would run, it would return with the incorrect intended responses! \n \nOption 2 contained 'int.input())', it needed to be 'int(input()). Option 2 also had the '<' and '>' symbols the incorrect way around! \n \nThank you for participating within this study! If you would like to read the dissertation that is connected to this research artefact then please send an email expressing interest in this to CN196703@falmouth.ac.uk and I will send you a copy once completed!"

            e "Take a look at this quick video, it will assist you in the upcoming question."

            $ renpy.movie_cutscene("Dramatic.webm")
            #Question 3
            e "The following exercise is a similar exercise based around branches. The following code is trying to create a variable representing the user's height and give a response to the user's input based on their height. See if you can find the errors within the code."

            e "print(\"How tall are you?\")
            \nheight == int(input())
            \n
            \nif height <= 166
            \n___print (\'You're allowed to ride without an adult!\')
            \nelif height > 152:
            \n___print (\"You're allowed to ride but must be accompanied by an adult!\")
            \nelif:
            \n___print (\"Sorry! You're too small to ride on this!\")"

            menu:

                # Incorrect answer
                "print(\"How tall are you?\")
                \nheight == int(input())
                \n
                \nif height >= 166:
                \n___print (\"Sorry! You're too small to ride on this!\")
                \nelse height > 152:
                \n___print (\"You're allowed to ride without an adult!\")
                \nelse:
                \n___print (\"You're allowed to ride but must be accompanied by an adult!\")":
                    jump IncorrectAnswer

                # Incorrect answer
                "print(\"How tall are you?\")
                \nheight = int.input())
                \n
                \nif height <= (\"166\"):
                \n___print (\"You're allowed to ride without an adult!\")
                \nelif height < 152:
                \n___print (\"You're allowed to ride but must be accompanied by an adult!\")
                \nelse:
                \n___print (\"Sorry! You're too small to ride on this!\")":
                    jump IncorrectAnswer

                # Correct answer
                "print(\"How tall are you?\")
                \nheight = int(input())
                \n
                \nif height >= 166:
                \n___print (\"You're allowed to ride without an adult!\")
                \nelif height > 152:
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
