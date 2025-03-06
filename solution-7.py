# Task 1
def index_min(L):
    # Find the index of the minimum element in the list L
    min_index = 0
    for x in range(1, len(L)):
        if L[x] <= L[min_index]:
            min_index = x
    return min_index

# Task 2 a)
def temp_decrease(L):
    # Find the largest temperature decrease in the list L
    decrease = 0
    for i in range(len(L) - 1):
        for j in range(i + 1, len(L)):
            if decrease < L[i] - L[j]:
                decrease = L[i] - L[j]
    return decrease

# Task 2 b)
def temp_decrease_fast(L):
    # Find the largest temperature decrease in the list L using an optimized approach
    decrease = 0
    max_index = 0
    for i in range(1, len(L)):
        if L[i] > L[max_index]:
            max_index = i
        elif decrease < L[max_index] - L[i]:
            decrease = L[max_index] - L[i]
    return decrease
