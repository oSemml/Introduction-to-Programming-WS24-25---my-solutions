import math

# Input the upper limit N
N = int(input())

# Initialize the list to mark prime numbers (1 means prime, 0 means not prime)
is_prime = [1] * N

# Sieve of Eratosthenes: Mark non-prime numbers
for i in range(2, int(math.ceil(math.sqrt(N)))):
    if is_prime[i] != 0:  # Check if 'i' is prime
        # Mark multiples of 'i' as non-prime
        for j in range(i * i, N, i):
            is_prime[j] = 0

# Print the count of prime numbers (excluding 0 and 1)
print(sum(is_prime) - 2)
