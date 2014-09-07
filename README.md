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
