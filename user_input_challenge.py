'''
##############################
User Input Challenge
##############################

Create a program that asks the user to enter their name and their age. Print out a message 
addressed to them that tells them the year that they will turn 100 years old.

Add on to the previous program by asking the user for another number and printing out that 
many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n" is the same as pressing the ENTER button)
'''
name = input("What is your name? ")
number1 = int(input("Enter your age. "))
val1 = int(input("How many times would you like the message to print? "))
number2 = 100
fix = -1
result = number1-number2
trueresult = result*fix
year = 2022
year100 = year+trueresult
text = f'You, {name}, will turn 100 in {year100}. \n' * val1
print(text)