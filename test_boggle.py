import unittest
import boggle

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
        
    def test_grid_cooerdinates(self):
        """
        Test to ensure that all coordinates inside grig can be accessed
        """
        
        grid = boggle.make_grid(2, 2)
        self.assertIn((0, 0), grid) #Use assertIn method to check if (0, 0) is in (2, 2) grid
        self.assertIn((0, 1), grid) #Use assertIn method to check if (0, 1) is in (2, 2) grid
        self.assertIn((1, 0), grid) #Use assertIn method to check if (1, 0) is in (2, 2) grid
        self.assertIn((1, 1), grid) #Use assertIn method to check if (1, 1) is in (2, 2) grid
        self.assertNotIn((2, 2), grid) #Use assertNotIn method to check if (2, 2) is not in (2, 2) grid
        