# package_dimensions.py

def find_package_dimensions(item_length, item_width, item_height, padding=2):
    """
    Calculate package dimensions based on item size.
    padding: extra space added for packaging material
    """
    package_length = item_length + padding
    package_width = item_width + padding
    package_height = item_height + padding
    return package_length, package_width, package_height

# Example usage
length = float(input("Enter item length: "))
width = float(input("Enter item width: "))
height = float(input("Enter item height: "))
# Validate input
if length <= 0 or width <= 0 or height <= 0:
    print("Error: Dimensions must be positive numbers!")
else:
    pkg_length, pkg_width, pkg_height = find_package_dimensions(length, width, height)
    print(f"Package dimensions: {pkg_length} x {pkg_width} x {pkg_height}")

