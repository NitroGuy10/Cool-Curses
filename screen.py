import curses

class screen:

    # The matrix contains the whole screen
    # The buffer contains what has changed since the last add_buffer() call

    def __init__(self, lines, cols, store_arrays=False) -> None:
        self.lines = lines
        self.cols = cols
        self.bottom_right_pos = (lines - 1, cols - 1)
        self.store_arrays = store_arrays
        self.clear()

    def clear(self):
        self.matrix_dict = {}
        self.buffer_dict = {}
        
        if self.store_arrays:
            self.matrix = self.empty_screen_array()
            self.buffer = self.empty_screen_array()
        
    def clear_and_add(self, stdscr):
        self.clear()
        self.add_matrix(stdscr)
    
    def empty_screen_array(self):
        return [[" "] * self.lines] * self.cols
    
    def __getitem__(self, indices):
        if isinstance(indices, tuple) and len(indices) == 2:
            if (indices[0], indices[1]) in self.matrix_dict:
                return self.matrix_dict[(indices[0], indices[1])]
            else:
                return " "
        else:
            raise IndexError("A y and x must be supplied")
    
    def __setitem__(self, indices, value) -> None:
        if isinstance(indices, tuple) and len(indices) == 2:
            line = indices[0]
            col = indices[1]

            # Due to the curses "bottommost-rightmost character" quirk,
            # do not insert any characters into that position
            if line == self.lines - 1 and col == self.cols - 1:
                return

            self.buffer_dict[(line, col)] = value
            if value == " " and (line, col) in self.matrix_dict:
                del self.matrix_dict[(line, col)]
            else:
                self.matrix_dict[(line, col)] = value
            
            if self.store_arrays:
                self.matrix[line][col] = value
                self.buffer[line][col] = value
        else:
            raise IndexError("A y and x must be supplied")

    def add_matrix(self, stdscr) -> None:
        for line in range(self.lines):
            for col in range(self.cols):
                if line == self.lines - 1 and col == self.cols - 1:
                    continue

                if (line, col) in self.matrix_dict:
                    stdscr.addch(line, col, self.matrix_dict[(col, line)])
                else:
                    stdscr.addch(line, col, " ")


    def add_buffer(self, stdscr) -> None:
        self.add_buffer_without_clearing_it(stdscr)

        self.buffer_dict = {}
        if self.store_arrays:
            self.buffer = self.empty_screen_array()

    def add_buffer_without_clearing_it(self, stdscr) -> None:
        for position, char in self.buffer_dict.items():
            stdscr.addch(position[0], position[1], char)
   
    def __print_screen(self, screen_dict) -> None:
        for line in range(self.lines):
            for col in range(self.col):
                if (line, col) in self.matrix_dict:
                    print(self.matrix_dict[(line, col)], end="")
                else:
                    print(" ", end="")
            print()
            

    def print_matrix(self) -> None:
        self.__print_screen(self.matrix_dict)

    def print_buffer(self) -> None:
        self.__print_screen(self.buffer_dict)
