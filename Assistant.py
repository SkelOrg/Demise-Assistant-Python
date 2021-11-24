import sys
sys.dont_write_bytecode = True
import pylib

print("Welcome, User!")
pylib.text_to_speech("Welcome, User!")
print("Commands may be typed below. (Type 'help' to see all commands).")

while True:
    maincommands = input()

    if maincommands == "help" or maincommands == "'help'":
        print("Here's some help.")
        pylib.text_to_speech("Here's some help.")
        print("Commands: note, clock, quit, sourcecode, webapp")
    elif maincommands == "quit":
        sys.exit(0)
    elif maincommands == "clock":
        print("Here's the time.")
        pylib.text_to_speech("Here's the time.")
        print(f"The time is: {pylib.getTime()}")
    elif maincommands == "note":
        print("Opening 'Note'.")
        pylib.text_to_speech("Opening 'Note'.")
        pylib.create_note()
    elif maincommands == "sourcecode":
        print("Opening sourcecode.")
        pylib.text_to_speech("Opening sourcecode.")
        pylib.openUrl("https://github.com/Skelebrine/Demise-Assistant-Python")
    elif maincommands == "webapp":
        chosenwebapp = input("Which webapp would you like to open? (Type 'help' for a list of webapps.) ")
        if chosenwebapp == "help":
            print("Here's a list of webapps.")
            pylib.text_to_speech("Here's a list of webapps.")
            print("Webapps: discord, youtube, spotify, other")
        elif chosenwebapp == "discord":
            print("Opening Discord.")
            pylib.text_to_speech("Opening Discord.")
            pylib.openUrl("https://app.discord.com")
        elif chosenwebapp == "youtube":
            print("Opening YouTube.")
            pylib.text_to_speech("Opening YouTube.")
            pylib.openUrl("https://www.youtube.com")
        elif chosenwebapp == "spotify":
            print("Opening Spotify.")
            pylib.text_to_speech("Opening Spotify.")
            pylib.openUrl("https://open.spotify.com")
        elif chosenwebapp == "other":
            givenurl = input("Please enter the URL of the webapp you would like to open: ")
            websitetitle = pylib.getWebsiteTitle(givenurl)
            print(f"Opening '{websitetitle}'.")
            pylib.text_to_speech(f"Opening '{websitetitle}'.")
            pylib.openUrl(givenurl)
        else:
            print("That's not a webapp.")
    else:
        print("That isn't a command. Enter 'help' to get a list of available commands.")
