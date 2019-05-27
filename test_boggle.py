import unittest
import boggle
from string import ascii_uppercase

class TestBoggle(unittest.TestCase):
    """
    Our test suite for boggle solver
    """

    def test_can_create_an_empty_grid(self):
        """
        Test to see if we can create an empty grid
        """
        grid = boggle.make_grid(0, 0)
        self.assertEqual(len(grid), 0)
        
    def test_grid_size_is_row_times_Column(self):
        """
        Test is to show that the total size of the grid is equal to width * height
        """
        grid = boggle.make_grid(2, 3)
        self.assertEqual(len(grid), 6)
        
    def test_grid_coordinates(self):
        """
        Test to ensure that all coordinates inside grig can be accessed
        """
        
        grid = boggle.make_grid(2, 2)
        self.assertIn((0, 0), grid) #Use assertIn method to check if (0, 0) is in (2, 2) grid
        self.assertIn((0, 1), grid) #Use assertIn method to check if (0, 1) is in (2, 2) grid
        self.assertIn((1, 0), grid) #Use assertIn method to check if (1, 0) is in (2, 2) grid
        self.assertIn((1, 1), grid) #Use assertIn method to check if (1, 1) is in (2, 2) grid
        self.assertNotIn((2, 2), grid) #Use assertNotIn method to check if (2, 2) is not in (2, 2) grid
        
    def test_grid_is_filled_with_letters(self):
        """
        Ensure that each of the coordinates in the grid
        contain letters
        """
        grid = boggle.make_grid(2, 3)
        for letter in grid.values():
            self.assertIn(letter, ascii_uppercase)