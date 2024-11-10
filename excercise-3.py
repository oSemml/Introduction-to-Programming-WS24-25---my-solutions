# Read two lists of integers from input
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

# For each number in list 'a'
for x in a:
    # For each number in list 'b'
    for y in b:
        # Check if 'x' is divisible by 'y'
        if x % y == 0:
            print(x)  # Print 'x' if it's divisible by any 'y'
            break  # Exit the inner loop after finding the first divisor