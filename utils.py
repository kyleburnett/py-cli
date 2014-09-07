from cli import *

def sayHello():
    print "Hello"
    raw_input("Press Enter to continue")

def constructObject():
    name = getStringInput("Enter your name: ")
    age = getNumberInput("Enter your age: ")
    blue = getBooleanInput("Do you like the color blue (y/n): ", "y/n")
    obj = { "name": name, "age": age, "blue": blue };
    print obj
    raw_input("Press Enter to continue")