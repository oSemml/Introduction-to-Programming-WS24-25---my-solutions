# Function to solve quadratic equations of the form ax^2 + bx + c = 0
def zeros(a, b, c):
    # If the coefficient 'a' is 0, it's not a quadratic equation, so return without doing anything
    if a == 0:
        return
    
    # Calculate the discriminant (disk) to determine the nature of the roots
    disk = b * b - 4 * a * c

    # If the discriminant is zero, there is exactly one real root (repeated)
    if disk == 0:
        # The single real root is given by -b / (2a)
        print(-b / (2 * a))
    
    # If the discriminant is positive, there are two distinct real roots
    elif disk > 0:
        # Calculate and print both roots using the quadratic formula
        print((-b + disk ** (1 / 2)) / (2 * a))  # First root
        print((-b - disk ** (1 / 2)) / (2 * a))  # Second root
    
    # If the discriminant is negative, the equation has no real solutions
    else:
        print("Es gibt keine reellen Nullstellen")  # German message: "There are no real roots"

# Test cases
zeros(1, 1, 1)  # Example where there are no real solutions
zeros(1, 2, 1)  # Example where there is exactly one real solution
zeros(1, 3, 1)  # Example where there are two distinct real solutions
