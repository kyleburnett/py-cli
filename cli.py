import os

##################################################
# Main class

class CLI():
    """
    The command line interface (CLI)
    """
    def __init__(self, header="########################################"):
        self._header = header
        self._menuoptions = []

    def addMenuOption(self, option):
        """
        Adds a menu option to the CLI's main menu

        Arguments:
            option: (MenuOption|SubMenuOption) - The menu option instance

        Raises:
            TypeError
        """
        # Error handle option
        if not isinstance(option, MenuOption):
            raise TypeError("The argument must be an instance of MenuOption")

        # Append to the list of menu options
        self._menuoptions.append(option)

    def callAction(self, selection):
        """
        Calls the function associated with the given action
        """
        self._menuoptions[selection]._action()

    def run(self):
        """
        Run the menu in a loop
        """
        printMenu(self._header, self._menuoptions)
        while True:
            char = raw_input("Make Selection >>> ")
            try:
                selection = int(char)
                if selection - 1 < 0:
                    raise ValueError("Select an option from the menu")
                self.callAction(selection - 1)
                printMenu(self._header, self._menuoptions)
            except:
                print "Invalid Selection. Try Again..."
                continue

##################################################
# Support Classes

class MenuOption():
    def __init__(self, prompt, action):
        self._prompt = prompt
        self._action = action

    def getPrompt(self):
        return self._prompt

##################################################
# Support Functions

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def getStringInput(message):
    return raw_input(message)

def getBooleanInput(message, format):
    options = format.split("/")
    if len(options) != 2:
        raise ValueError("Expected format of the form t/f")
    while True:
        chosen = raw_input(message)
        if chosen == options[0]:
            return True
        elif chosen == options[1]:
            return False
        else:
            print "Input must be one the given boolean values"

def getNumberInput(message):
    while True:
        number = raw_input(message)
        try:
            return int(number)
        except:
            print "Input must be number"

def printMenu(header, options):
    clear()
    i = 1
    print header
    for option in options:
        print str(i) + ". " + option.getPrompt()
        i += 1
    print ""