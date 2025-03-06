# Input: Number of disks
n = int(input())

# List to store the move sequences
moves = []

# Recursive function to solve Towers of Hanoi
def hanoi(n, Pol1, Pol2, Pol3):
    # If there are more than 1 disk, move n-1 disks
    if n > 1:
        hanoi(n - 1, Pol1, Pol3, Pol2)  # Move n-1 disks from source to auxiliary
        moves.append(Pol1 + Pol3)       # Move the nth disk from source to target
        hanoi(n - 1, Pol2, Pol1, Pol3)  # Move n-1 disks from auxiliary to target
    
    # If there is exactly 1 disk, move it directly
    if n == 1:
        moves.append(Pol1 + Pol3)

# Solve the puzzle: move disks from peg 'A' to peg 'C' using 'B' as auxiliary
hanoi(n, 'A', 'B', 'C')

# Output all moves as a comma-separated string
print(*moves, sep=',')
