import pygame
from constants import *
from cell import Cell

# Charles James Jr
class Board:
    # This class represents an entire Sudoku board. A Board object has 81 Cell objects.
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = [[Cell((0, row, col, screen)[i][j], i, j, self.height // 9,
                            self.width // 9) for j in range(9)] for i in
                      range(9)]
    # Constructor for the Board class.
    # screen is a window from PyGame.
    # difficulty is a variable to indicate if the user chose easy, medium, or hard.
    def draw(self):
        # draw lines
        for i in range(1, 9):
            pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE * i),
                             (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
        # draw vertical lines
        for i in range(1, 9):
            pygame.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE * i, 0),
                             (SQUARE_SIZE * i, HEIGHT), LINE_WIDTH)
        for i in range(self.width):
            for j in range(self.height):
                self.cells[i][j].draw(self.screen)

    # Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
    # Draws every cell on this board.
    def select(self, row, col):
        self.select = True

    # Marks the cell at (row, col) in the board as the current selected cell.
    # Once a cell has been selected, the user can edit its value or sketched value.
    def click(self, x, y):
        pass
# If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col)
# of the cell which was clicked. Otherwise, this function returns None.
