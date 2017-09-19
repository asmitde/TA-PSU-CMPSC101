import math

# Print the table header
print(format('Deg.', '<5s'), format('Sin', '<10.4s'), format('Cos', '<10.4s'))

# Initialize loop counter
deg = 0

while deg <= 360:
    # Convert degree to radians
    rad = math.radians(deg)
   
    # The round() function is to round of the values to 4 decimal places.
    # + 0 is used to remove the -ve sign for -0.0 values: -0.0 + 0 = 0.0. 
    sin = round(math.sin(rad), 4) + 0
    cos = round(math.cos(rad), 4) + 0

    # The values are again formatted with .4f to add trailing 0s to values
    # that had less than 4 precision places.
    print(format(deg, '<5d'), format(sin, '<10.4f'), format(cos, '<10.4f'))

    # Increment loop counter
    deg += 10
