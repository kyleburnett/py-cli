py-cli
======

A menu-based python command line interface constructor tool

Getting Started
-------

Download cli.py and include it in your project. Make sure there is a __init__.py script in your project. Import and use the module as follows:

```
from cli import *

cli = CLI("Welcome!")

cli.run()
```

When you run this script, you will see the message `Welcome!` printed on the console followed by a prompt for input. To exit use `Ctrl+C`.

CLI API
-------

### class CLI(header)

Creates and returns an instance of the CLI class.

 * <i>header</i>: A string to serve as the menu header.

### CLI#addMenuOption(option)

Adds an option to the menu.

 * <i>option</i>: An instance of the class `MenuOption`. See below in the Supporting Classes and Functions section.

### CLI#callAction(selection)

Calls the `i`th menu option given by the integer `selection`. The options are indexed at 0.

### CLI#run()

Starts the command line interface.

Supporting Classes and Functions
-------

### class MenuOption(prompt, action)

Creates and returns a menu option.

 * <i>prompt</i>: a string of menu prompt text for the given menu option
 * <i>action</i>: a function to call

### clear()

Clears the console.

### getStringInput(message)

Gets string input from the user using the given prompt text.

 * <i>message</i>: the prompt text.

### getBooleanInput(message, format)

Gets a True or False value from the user using a character specified in `format`.

 * <i>message</i>: the prompt text.
 * <i>format</i>: a string of the form `@/$` where the `@` and `$` symbols refer to distinct characters representing distinct True/False values.

### getNumberInput(message, format)

Gets number input from the user using the given prompt text.

 * <i>message</i>: the prompt text.

### printMenu(header, options)

Prints a header followed by the menu options.

 * <i>header</i>: a string header
 # <i>options</i>: a list of `MenuOption` instances or any other object with a getPrompt() method

Examples
-------

See `test.py` and `utils.py` for example's of the module's use.
