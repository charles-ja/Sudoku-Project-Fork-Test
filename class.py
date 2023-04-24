# Charles James Jr
class Cell:
    # This class represents a single cell in the Sudoku board. There are 81 Cells in a Board.
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0

        self.selected = False

    # Constructor for the Cell class

    def set_cell_value(self, value):
        self.value = value

    # Setter for this cell’s value

    def set_sketched_value(self, value):
        self.sketched_value = value

    # Setter for this cell’s sketched value
    def draw(self):
        width = 25
        height = 25
        number_font = pygame.font.Font(None, 400)
        number_surf = number_font.render(self.value, True, CROSS_COLOR)
        if self.value != 0:
            number_rect = number_surf.get_rect(
                center=(self.row // 2 + width * self.col,
                        height // 2 + height * self.row))
            self.screen.blit(number_surf, number_rect)
