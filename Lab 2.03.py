'''
##########################################
Lab 2.03 - Game Show
##########################################
In your Notebook
Follow the flow of execution in the following programs and predict what will happen for each
one
---------------------------------------
Example 1
---------------------------------------
a = input("What... is your quest")
b = "to seek the holy grail"
if a != b:
    print("Go On. Off you go")
else:
    b = input("What...is the air-speed velocity of an unladen swallow?")
    if b == "What do you mean? An African or European swallow?":
        print("I don't know that...AHHH [Bridgekeeper was thrown over bridge]")
    else:
        print("[you were thrown over bridge]")

Prediction: It will function as written.
Actual: It simply skipps directly to the first print command no matter the input.

---------------------------------------
Example 2
---------------------------------------
user_input = input("What is your favorite color")
if user_input == 'blue':
    print("Blueskadoo")
elif user_input == "red":
    print("Roses are red!")
elif user_input == "yellow":
    print("Mellow Yellow")
elif user_input == "green":
    print("Green Machine")
elif user_input == "orange":
    print("Orange you glad I didn't say banana.")
elif user_input == "black":
    print("I see a red door and I want it painted black")
elif user_input == "purple":
    print("And we'll never be royalllssss")
elif user_input == "pink":
    print("Pinky- and the Brain")
else:
    print("I don't recognize that color. Is it even...??")

Prediction: It will function as intended.
Actual: It does work.

---------------------------------------
In your Notebook
---------------------------------------
Translate this Snap! program into a Python program
***Refer to the image provided on Moodle located below the Lab 2.03 link***
Write program below:

---------------------------------------
Create a game show program
---------------------------------------
Declare 10 prizes (prize1, prize2, prize 3 at the top of your file)
User picks a number
The prize corresponding with that door is printed for the user.
Write code below the multiline comment
'''
prize1 = "$1"
prize2 = "$2"
prize3 = "$3"
prize4 = "$4"
prize5 = "$5"
prize6 = "$6"
prize7 = "$7"
prize8 = "$8"
prize9 = "$9"
prize10 = "$10"
user_input = input("What door do you pick? (1-10) ")
if user_input == '1':
    print({prize1})
elif user_input == "2":
    print({prize2})
elif user_input == "3":
    print({prize3})
elif user_input == "4":
    print({prize4})
elif user_input == "5":
    print({prize5})
elif user_input == "6":
    print({prize6})
elif user_input == "7":
    print({prize7})
elif user_input == "8":
    print({prize8})
elif user_input == "9":
    print({prize9})
elif user_input == "10":
    print({prize10})
else:
    print("That isn't an option.")