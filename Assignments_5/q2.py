# Define a function 'rectangle_stats' that accepts 'length' and 'width' parameters
def rectangle_stats(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Prompt the user for the length and width, converting inputs to floats
length_input = float(input("Enter the length: "))
width_input = float(input("Enter the width: "))

# Call the function and store the returned results in two variables
area_result, perimeter_result = rectangle_stats(length_input, width_input)

# Print both results using f-strings, each rounded to two decimal places
print(f"Area: {area_result:.2f}")
print(f"Perimeter: {perimeter_result:.2f}")
