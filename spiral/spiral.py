import curses
# https://docs.python.org/3/howto/curses.html
import math

# stdscr = curses.initscr()
# curses.noecho()  # Don't echo keystrokes to the screen
# curses.cbreak()  # Respond to input immediately, without having to press ENTER first
# stdscr.keypad()  # Make curses interpret keypad keys for me

# # End program
# curses.nocbreak()
# stdscr.keypad(False)
# curses.echo()
# curses.endwin()

# Or just have the wrapper do it for me
def main(stdscr: curses.window):
    stdscr.clear()  # Clear screen
    curses.curs_set(0)

    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_MAGENTA , curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_WHITE , curses.COLOR_BLACK)

    radius = 1
    angle = 0

    while (radius > 0):
        x_pos = (math.cos(angle) * radius + 1) * (curses.COLS - 1) / 2
        y_pos = (math.sin(angle) * radius + 1) * (curses.LINES - 1) / 2
        color_pair_num = math.floor(((angle / (2*math.pi)) % 1) * 6) + 1
        #color_pair_num = 7

        if not (0 <= x_pos < curses.COLS):
            break
        if not (0 <= y_pos < curses.LINES):
            break

        stdscr.addch(round(y_pos), round(x_pos), "O", curses.color_pair(color_pair_num))

        angle += 0.05
        radius -= 0.001

        stdscr.refresh()
        curses.napms(2)
    
    stdscr.refresh()

    radius = 1
    angle = 0

    while (radius > 0):
        x_pos = (math.cos(angle) * radius + 1) * (curses.COLS - 1) / 2
        y_pos = (math.sin(angle) * radius + 1) * (curses.LINES - 1) / 2
        # color_pair_num = math.floor(((angle / (2*math.pi)) % 1) * 6) + 1
        color_pair_num = 7

        if not (0 <= x_pos < curses.COLS):
            break
        if not (0 <= y_pos < curses.LINES):
            break

        stdscr.addch(round(y_pos), round(x_pos), " ", curses.color_pair(color_pair_num))

        angle += 0.05
        radius -= 0.001

        stdscr.refresh()
        curses.napms(2)
    
    stdscr.refresh()


    # pos = 0
    # while (pos < curses.COLS and pos < curses.LINES):
    #     stdscr.addch(pos, pos, "A")
    #     pos += 1

    while True:
        pass


    



curses.wrapper(main)

