#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import pyperclip

INITIAL_VARS = None  # set the name in global scope to make it appear within itself
VERSION = "0.2.0"
HELP_SHORT = """
- \033[1mAVAILABLE VALUES\033[0m -----------------------
 _           references last output
 pi, e, gr   π, euler's nmbr, golden ratio

- \033[1mMATH FUNCTIONS\033[0m -------------------------
'* from math' is imported by default, for
documentation see here:
http://docs.python.org/2/library/math.html

 functions() shows a list of all available
             math functions

- \033[1mOTHER FUNCTIONS\033[0m ------------------------
 cp()      - copy last value to clipboard
 vars()    - show all user-set variables
 help()    - view this text
 help(fun) - view help for a specific
             function, e.g. help(log10)

Type exit() or use Ctrl-D to quit
"""

class _BCOLORS:
    """
    Used for colored terminal output
    """
    HEADER = '\033[1m\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def _init():
    """
    Initialize PyCalc
    """
    _init_globals()
    clear()
    print('%sPyCalc v.%s%s' % (_BCOLORS.HEADER, VERSION, _BCOLORS.ENDC))
    help()

def _init_globals():
    """
    Make some functions and constants available to the user
    """
    # import * from math to global
    math_module = __import__('math')
    globals().update(math_module.__dict__)

    # other constants
    globals()['gr'] = (1+sqrt(5))/2  # The golden ratio

def clear():
    """
    Clear all output
    """
    print(chr(27) + "[2J")


def cp():
    """
    Copy last output to clipboard
    """
    pyperclip.copy(unicode(_))

def functions():
    """
    Print all functions available in the math module
    """
    for attr_name in dir(math):
        attr = getattr(math, attr_name)
        if hasattr(attr, '__call__'):  # is a function?
            print(attr.__doc__.split('\n')[0]) # first line of __doc__

def vars():
    """
    Print names and values of all user-set variables
    """
    for local, value in globals().iteritems():
        if local not in INITIAL_VARS:
            print('%s = %s%s%s' % (local, _BCOLORS.OKBLUE, value, _BCOLORS.ENDC))

def help(method = None):
    """
    Display usage instructions.

    If no parameter is given, general instructions are shown.
    If the parameter is a function, help for the given function is shown.
    """
    if hasattr(method, '__call__'):  # is a function?
        if method.__doc__ is None:
            print('No documentation for %s' % method.__name__)
        else:
            print(method.__doc__)
    else:
        print(HELP_SHORT)


if __name__ == '__main__':
    _init()

    # INITIAL_VARS is used to distinguish user set variables in vars().
    #
    # Setting it from globals() should be the last thing before handing over
    # to the user. All variables names added to global scope after this step
    # will be seen as set by the user.
    INITIAL_VARS = tuple(globals().keys())
