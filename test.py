from cli import *
import utils

cli = CLI("""
####################################
# Welcome! Please make a selection #
####################################""")

cli.addMenuOption(MenuOption("Get a greeting", utils.sayHello))
cli.addMenuOption(MenuOption("Enter an object", utils.constructObject))

cli.run()