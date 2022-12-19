import curses
import math
import screen

def main(stdscr: curses.window):
    stdscr.clear() 
    curses.curs_set(0)

    radius = 1
    angle = 0
    MOVING_CHAR = "O"
    STILL_CHAR = "█"

    main_screen = screen.screen(curses.LINES, curses.COLS)

    while (radius > 0):
        x_pos = (math.cos(angle) * radius + 1) * (curses.COLS - 1) / 2
        y_pos = (math.sin(angle) * radius + 1) * (curses.LINES - 1) / 2
        # color_pair_num = math.floor(((angle / (2*math.pi)) % 1) * 6) + 1
        color_pair_num = 7

        if not (0 <= x_pos < curses.COLS):
            break
        if not (0 <= y_pos < curses.LINES):
            break

        main_screen[round(y_pos), round(x_pos)] = MOVING_CHAR

        angle += 0.05
        radius -= 0.001

        main_screen.add_buffer(stdscr)
        stdscr.refresh()
        curses.napms(2)
    
    stdscr.refresh()

    radius = 1
    angle = 0

    for iteration in range(curses.LINES):
        
        dict_items = tuple(main_screen.matrix_dict.items())
        for coords, char in dict_items: 
            if char == STILL_CHAR:
                continue

            line = coords[0]
            col = coords[1]

            if line == curses.LINES - 1:
                main_screen[line, col] = STILL_CHAR
            else:
                main_screen[line, col] = " "
                line += 1
                main_screen[line, col] = MOVING_CHAR
                if line == curses.LINES - 1:
                    main_screen[line, col] = STILL_CHAR
        
        for coords, char in main_screen.matrix_dict.items(): 
            if char == STILL_CHAR:
                continue

            line = coords[0]
            col = coords[1]

            if main_screen[line + 1, col] == STILL_CHAR:
                main_screen[line, col] = STILL_CHAR

        main_screen.add_buffer(stdscr)
        stdscr.refresh()
        curses.napms(30)
    
    stdscr.refresh()

    curses.napms(1000)


curses.wrapper(main)
