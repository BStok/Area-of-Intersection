"""
Module to calculate the area of intersection between two rectangles.
Each rectangle is defined by two diagonally opposite corner coordinates.
"""


def calculate_intersection_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    """
    Calculate the area of intersection between two rectangles.
    
    Args:
        ax1, ay1: First corner of rectangle A
        ax2, ay2: Second corner of rectangle A
        bx1, by1: First corner of rectangle B
        bx2, by2: Second corner of rectangle B
    
    Returns:
        float: Area of intersection (0 if rectangles don't intersect)
    
    Raises:
        ValueError: If any coordinate is not a number
    """
    # Validate inputs
    try:
        coords = [ax1, ay1, ax2, ay2, bx1, by1, bx2, by2]
        for coord in coords:
            float(coord)
    except (TypeError, ValueError):
        raise ValueError("All coordinates must be numbers")
    
    # Normalize rectangle coordinates (ensure min < max)
    a_left = min(ax1, ax2)
    a_right = max(ax1, ax2)
    a_bottom = min(ay1, ay2)
    a_top = max(ay1, ay2)
    
    b_left = min(bx1, bx2)
    b_right = max(bx1, bx2)
    b_bottom = min(by1, by2)
    b_top = max(by1, by2)
    
    # Find intersection rectangle coordinates
    inter_left = max(a_left, b_left)
    inter_right = min(a_right, b_right)
    inter_bottom = max(a_bottom, b_bottom)
    inter_top = min(a_top, b_top)
    
    # Check if there is an intersection
    if inter_left >= inter_right or inter_bottom >= inter_top:
        return 0
    
    # Calculate area
    width = inter_right - inter_left
    height = inter_top - inter_bottom
    area = width * height
    
    return area