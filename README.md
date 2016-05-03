# pycalc

After searching for the perfect calculator app for the mac desktop, i ended up with the python shell.

To make things a little bit easier, i use a python script to do some setup and provide helpers. It's packaged into a mac app using [appify](https://github.com/subtleGradient/tilde-bin/blob/master/appify).

It loads the math library into global namespace and offers some helper functions.

## Usage
```
PyCalc v.0.2.0

- AVAILABLE VALUES -----------------------
 _           references last output
 pi, e, gr   π, euler's nmbr, golden ratio

- MATH FUNCTIONS -------------------------
'* from math' is imported by default, for
documentation see here:
http://docs.python.org/2/library/math.html

 functions() shows a list of all available
             math functions

- OTHER FUNCTIONS ------------------------
 cp()      - copy last value to clipboard
 vars()    - show all user-set variables
 help()    - view this text
 help(fun) - view help for a specific
             function, e.g. help(log10)

Type exit() or use Ctrl-D to quit

>>> _
```

## Installing
Make sure you have the necessary dependency installed: `pip install pyperclip`.
Then just drag PyCalc.app into your applications folder.
