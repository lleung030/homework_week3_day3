# Create a function that given a list of numbers (non-sorted) find the lowest number in the list and return it.
# Example Input: [50,30,4,2,11,0]
# Example Output: 0
# Example Input 2: [40,3,4,2]
# Example Output 2: 2

def low(lst):
    x = sorted(lst)
    return x[0]

print(low([50,30,40,2,11,0]))
print(low([40,3,4,2]))

        