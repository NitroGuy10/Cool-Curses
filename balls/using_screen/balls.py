import curses
from balls.ball import ball
import screen
import random

KEY_INPUT = True
GRAVITY = 0.001
RANDOM_CHARS = False
BALL_CHAR = "█"
DELTA_TIME_MS = 1
NUM_BALLS = 50

def randomRadius(radius):
    return random.random() * radius * 2 - radius

def main(stdscr: curses.window):
    stdscr.clear() 
    curses.curs_set(0)
    stdscr.nodelay(True)

    main_screen = screen.screen(curses.LINES, curses.COLS)

    balls = []
    #balls.append(ball(curses.COLS / 2, curses.LINES / 2, 0.09, -0.05, 0.0, 0.0004, curses.COLS, curses.LINES))
    for i in range(NUM_BALLS):
        if RANDOM_CHARS:
            balls.append(ball(random.random() * (curses.COLS - 1),  random.random() * (curses.LINES - 1), randomRadius(0.1), randomRadius(0.1), 0.0, GRAVITY, 0.8 + randomRadius(0.05), curses.COLS, curses.LINES, chr(random.randint(33, 126))))
        else:
            balls.append(ball(random.random() * (curses.COLS - 1),  random.random() * (curses.LINES - 1), randomRadius(0.1), randomRadius(0.1), 0.0, GRAVITY, 0.8 + randomRadius(0.05), curses.COLS, curses.LINES, BALL_CHAR))


    while True:
        main_screen.clear_and_add(stdscr)

        if KEY_INPUT:
            key = stdscr.getch()
            if key == curses.KEY_UP:
                for ball_ in balls:
                    ball_.x_acc = 0
                    ball_.y_acc = -GRAVITY
            elif key == curses.KEY_DOWN:
                for ball_ in balls:
                    ball_.x_acc = 0
                    ball_.y_acc = GRAVITY
            elif key == curses.KEY_LEFT:
                for ball_ in balls:
                    ball_.x_acc = -GRAVITY
                    ball_.y_acc = 0
            elif key == curses.KEY_RIGHT:
                for ball_ in balls:
                    ball_.x_acc = GRAVITY
                    ball_.y_acc = 0

        for ball_ in balls:
            ball_.update(DELTA_TIME_MS)
            ball_.display(main_screen)

        main_screen.add_buffer(stdscr)
        stdscr.refresh()
        curses.napms(DELTA_TIME_MS)


curses.wrapper(main)
