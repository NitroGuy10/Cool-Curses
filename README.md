# Cool-Curses

Fun graphical demos in the terminal with [Curses](https://docs.python.org/3/howto/curses.html).

Written in Python for no reason other than convenience.

## Usage

Clone the repository and make sure you have [Python 3](https://www.python.org/) installed.

If you're on Windows, install [windows-curses](https://pypi.org/project/windows-curses/) (tested with version 2.3.1):

```
pip3 install windows-curses
```

NOTE: The speed of these demos has been found to vary GREATLY from environment to environment. In general, they seem to run fast on MacOS, decently in WSL, and very slowly on Windows.

Run a demo using one of the following commands (on windows, use "py" instead of "python3"):

```
python3 main.py balls
python3 main.py balls auto
python3 main.py spiral
python3 main.py spiral_sand
```

My favorite is "python3 main.py balls".
You can control the direction of gravity using the arrow keys.
I use it like a fidget toy when I'm bored in class.

:)
