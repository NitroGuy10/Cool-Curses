from curses import color_pair

# TODO
#
# Have many balls that can bounce around inside the window
# Each ball has a position, velocity, and acceleration
# Balls do not collide with other balls
# But they do bounce off the edges of the screen
# Optionally I can give each ball a small amount of randomness/offset in its acceleration
#
# Use the arrow keys to set the direction of gravity
# Press space to spawn new balls
# Press backspace to delete balls
# 

class ball:
    def __init__(self, x_pos, y_pos, x_vel, y_vel, x_acc, y_acc, dampen, screen_cols, screen_lines, char="█", color_pair=7) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.x_acc = x_acc
        self.y_acc = y_acc
        self.dampen = dampen
        self.color_pair = color_pair

        self.screen_cols = screen_cols
        self.screen_lines = screen_lines
        self.char = char
    
    def display(self, stdscr):
        rounded_y_pos = round(self.y_pos)
        rounded_x_pos = round(self.x_pos)
        if not(rounded_y_pos == self.screen_lines - 1 and rounded_x_pos == self.screen_cols - 1):
            stdscr.addch(rounded_y_pos, rounded_x_pos, self.char, color_pair(self.color_pair))
    
    def update(self, deltaTime):
        if not(0 <= round(self.x_pos + self.x_vel * deltaTime) < self.screen_cols):
            self.x_vel *= -1 * self.dampen

        if not(0 <= round(self.y_pos + self.y_vel * deltaTime) < self.screen_lines):
            self.y_vel *= -1 * self.dampen

        self.x_pos += self.x_vel * deltaTime
        self.y_pos += self.y_vel * deltaTime
        self.x_vel += self.x_acc * deltaTime
        self.y_vel += self.y_acc * deltaTime

        
            




