def make_grid(width, height):
    """
   Create grid that will hold the tiles for the boggle game
    """
    return {(row, col): " " for row in range(height)
        for col in range(width)
    }