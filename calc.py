"""
Interactive script to calculate rectangle intersection areas.
Uses the rectangle_intersection module.
"""

from RectangleIntersection import calculate_intersection_area


def get_rectangle_input(rect_num):
    """
    Get diagonal corner coordinates from user for a rectangle.
    
    Args:
        rect_num: Rectangle number (1 or 2)
    
    Returns:
        tuple: (x1, y1, x2, y2) coordinates
    """
    while True:
        try:
            coords_str = input(
                f"Enter rectangle {rect_num} diagonal points (x1 y1 x2 y2): "
            )
            coords = list(map(float, coords_str.split()))
            
            if len(coords) != 4:
                print("Error: Please enter exactly 4 numbers separated by spaces.")
                continue
            
            return tuple(coords)
        except ValueError:
            print("Error: Please enter valid numbers.")


def main():
    """Main interactive loop."""
    print("=" * 60)
    print("Rectangle Intersection Area Calculator")
    print("=" * 60)
    print("Enter diagonal corner points for each rectangle.")
    print("Format: x1 y1 x2 y2")
    print()
    
    while True:
        try:
            # Get input for both rectangles
            x1, y1, x2, y2 = get_rectangle_input(1)
            x3, y3, x4, y4 = get_rectangle_input(2)
            
            # Calculate intersection area
            area = calculate_intersection_area(x1, y1, x2, y2, x3, y3, x4, y4)
            
            # Display result
            print("\n" + "-" * 60)
            print(f"Rectangle A: ({x1}, {y1}) to ({x2}, {y2})")
            print(f"Rectangle B: ({x3}, {y3}) to ({x4}, {y4})")
            print(f"Intersection Area: {area}")
            print("-" * 60 + "\n")
            
            # Ask if user wants to continue
            choice = input("Calculate another intersection? (yes/no): ").strip().lower()
            if choice not in ['yes', 'y']:
                print("Goodbye!")
                break
        
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            continue


if __name__ == "__main__":
    main()