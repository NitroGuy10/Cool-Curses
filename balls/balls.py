import curses
from balls.ball import ball
import random
import sys

KEY_INPUT = True
GRAVITY = 0.0003
RANDOM_CHARS = False
BALL_CHAR = "█"
DELTA_TIME_MS = 1
NUM_BALLS = 50
COLORS = True
AUTO = False
AUTO_FLIP_INTERVAL = 1000

def randomRadius(radius):
    return random.random() * radius * 2 - radius

def gravity_up(balls):
    for ball_ in balls:
        ball_.x_acc = 0
        ball_.y_acc = -GRAVITY

def gravity_down(balls):
    for ball_ in balls:
        ball_.x_acc = 0
        ball_.y_acc = GRAVITY

def gravity_left(balls):
    for ball_ in balls:
        ball_.x_acc = -GRAVITY
        ball_.y_acc = 0

def gravity_right(balls):
    for ball_ in balls:
        ball_.x_acc = GRAVITY
        ball_.y_acc = 0

def main(stdscr: curses.window):
    global AUTO
    if "auto" in sys.argv:
        AUTO = True

    stdscr.clear() 
    curses.curs_set(0)
    stdscr.nodelay(True)

    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_MAGENTA , curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_WHITE , curses.COLOR_BLACK)

    balls = []
    #balls.append(ball(curses.COLS / 2, curses.LINES / 2, 0.09, -0.05, 0.0, 0.0004, curses.COLS, curses.LINES))
    for i in range(NUM_BALLS):
        color_pair = 7
        if COLORS:
            color_pair = random.randint(1, 7)

        this_ball_char = BALL_CHAR
        if RANDOM_CHARS:
            this_ball_char = chr(random.randint(33, 126))
        
        balls.append(ball(random.random() * (curses.COLS - 1),  random.random() * (curses.LINES - 1), randomRadius(0.1), randomRadius(0.1), 0.0, GRAVITY, 0.8 + randomRadius(0.05), curses.COLS, curses.LINES, this_ball_char, color_pair))

    KEY_INPUT_INTERVAL = 100 // DELTA_TIME_MS
    key_frame_counter = 0

    auto_flip_counter = 0
    auto_flip_direction = 0

    while True:
        stdscr.clear()

        if AUTO and auto_flip_counter == 0:
            if auto_flip_direction == 0:
                gravity_down(balls)
            elif auto_flip_direction == 1:
                gravity_right(balls)
            elif auto_flip_direction == 2:
                gravity_up(balls)
            else:
                gravity_left(balls)

            auto_flip_direction = (auto_flip_direction + 1) % 4


        if KEY_INPUT and key_frame_counter == 0:
            key = stdscr.getch()
            if key == curses.KEY_UP:
                gravity_up(balls)
            elif key == curses.KEY_DOWN:
                gravity_down(balls)
            elif key == curses.KEY_LEFT:
                gravity_left(balls)
            elif key == curses.KEY_RIGHT:
                gravity_right(balls)
                

        for ball_ in balls:
            ball_.update(DELTA_TIME_MS)
            ball_.display(stdscr)

        stdscr.refresh()
        curses.napms(DELTA_TIME_MS)
        key_frame_counter = (key_frame_counter + 1) % KEY_INPUT_INTERVAL
        auto_flip_counter = (auto_flip_counter + 1) % AUTO_FLIP_INTERVAL


curses.wrapper(main)
