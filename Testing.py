"""
Unit tests for the rectangle intersection area calculator.
Uses Python's unittest framework.
"""

import unittest
from RectangleIntersection import calculate_intersection_area


class TestRectangleIntersection(unittest.TestCase):
    """Test cases for rectangle intersection area calculation."""
    
    def test_no_intersection_complete_separation(self):
        """Test two rectangles that don't overlap at all."""
        # Rectangle A: (0,0) to (2,2), Rectangle B: (5,5) to (7,7)
        result = calculate_intersection_area(0, 0, 2, 2, 5, 5, 7, 7)
        self.assertEqual(result, 0)
    
    def test_no_intersection_touching_edge(self):
        """Test two rectangles that touch at an edge (no area intersection)."""
        # Rectangle A: (0,0) to (2,2), Rectangle B: (2,0) to (4,2)
        result = calculate_intersection_area(0, 0, 2, 2, 2, 0, 4, 2)
        self.assertEqual(result, 0)
    
    def test_no_intersection_touching_corner(self):
        """Test two rectangles that touch at a corner."""
        # Rectangle A: (0,0) to (2,2), Rectangle B: (2,2) to (4,4)
        result = calculate_intersection_area(0, 0, 2, 2, 2, 2, 4, 4)
        self.assertEqual(result, 0)
    
    def test_complete_overlap(self):
        """Test one rectangle completely inside another."""
        # Rectangle A: (0,0) to (10,10), Rectangle B: (2,2) to (4,4)
        result = calculate_intersection_area(0, 0, 10, 10, 2, 2, 4, 4)
        self.assertEqual(result, 4)  # 2x2 area
    
    def test_identical_rectangles(self):
        """Test two identical rectangles."""
        # Both: (0,0) to (3,3)
        result = calculate_intersection_area(0, 0, 3, 3, 0, 0, 3, 3)
        self.assertEqual(result, 9)  # 3x3 area
    
    def test_partial_overlap_horizontal(self):
        """Test two rectangles with partial horizontal overlap."""
        # Rectangle A: (0,0) to (4,2), Rectangle B: (2,0) to (6,2)
        result = calculate_intersection_area(0, 0, 4, 2, 2, 0, 6, 2)
        self.assertEqual(result, 4)  # 2x2 area
    
    def test_partial_overlap_vertical(self):
        """Test two rectangles with partial vertical overlap."""
        # Rectangle A: (0,0) to (2,4), Rectangle B: (0,2) to (2,6)
        result = calculate_intersection_area(0, 0, 2, 4, 0, 2, 2, 6)
        self.assertEqual(result, 4)  # 2x2 area
    
    def test_partial_overlap_both_axes(self):
        """Test two rectangles with partial overlap on both axes."""
        # Rectangle A: (0,0) to (4,4), Rectangle B: (2,2) to (6,6)
        result = calculate_intersection_area(0, 0, 4, 4, 2, 2, 6, 6)
        self.assertEqual(result, 4)  # 2x2 area
    
    def test_reversed_coordinates_rect_a(self):
        """Test with reversed diagonal points in rectangle A."""
        # Rectangle A: (2,2) to (0,0) [reversed], Rectangle B: (0,0) to (4,4)
        result = calculate_intersection_area(2, 2, 0, 0, 0, 0, 4, 4)
        self.assertEqual(result, 4)  # 2x2 area
    
    def test_reversed_coordinates_rect_b(self):
        """Test with reversed diagonal points in rectangle B."""
        # Rectangle A: (0,0) to (4,4), Rectangle B: (4,4) to (2,2) [reversed]
        result = calculate_intersection_area(0, 0, 4, 4, 4, 4, 2, 2)
        self.assertEqual(result, 4)  # 2x2 area
    
    def test_both_reversed_coordinates(self):
        """Test with reversed coordinates in both rectangles."""
        # Rectangle A: (4,4) to (0,0), Rectangle B: (6,6) to (2,2)
        result = calculate_intersection_area(4, 4, 0, 0, 6, 6, 2, 2)
        self.assertEqual(result, 4)  # 2x2 area
    
    def test_negative_coordinates(self):
        """Test with negative coordinates."""
        # Rectangle A: (-2,-2) to (2,2), Rectangle B: (0,0) to (4,4)
        result = calculate_intersection_area(-2, -2, 2, 2, 0, 0, 4, 4)
        self.assertEqual(result, 4)  # 2x2 area
    
    def test_floating_point_coordinates(self):
        """Test with floating-point coordinates."""
        # Rectangle A: (0.5,0.5) to (2.5,2.5), Rectangle B: (1.5,1.5) to (3.5,3.5)
        result = calculate_intersection_area(0.5, 0.5, 2.5, 2.5, 1.5, 1.5, 3.5, 3.5)
        self.assertAlmostEqual(result, 1.0)  # 1x1 area
    
    def test_zero_area_rectangle(self):
        """Test with a degenerate rectangle (zero area)."""
        # Rectangle A: (0,0) to (2,2), Rectangle B: (1,1) to (1,3) [zero width]
        result = calculate_intersection_area(0, 0, 2, 2, 1, 1, 1, 3)
        self.assertEqual(result, 0)
    
    def test_large_numbers(self):
        """Test with large coordinate values."""
        # Rectangle A: (0,0) to (1000,1000), Rectangle B: (500,500) to (1500,1500)
        result = calculate_intersection_area(0, 0, 1000, 1000, 500, 500, 1500, 1500)
        self.assertEqual(result, 250000)  # 500x500 area
    
    def test_invalid_input_string(self):
        """Test that invalid string input raises ValueError."""
        with self.assertRaises(ValueError):
            calculate_intersection_area("a", 0, 2, 2, 0, 0, 4, 4)
    
    def test_invalid_input_none(self):
        """Test that None input raises ValueError."""
        with self.assertRaises(ValueError):
            calculate_intersection_area(None, 0, 2, 2, 0, 0, 4, 4)


if __name__ == "__main__":
    # Run all tests with verbose output
    unittest.main(verbosity=2)