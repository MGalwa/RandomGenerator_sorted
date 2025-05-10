# Magdalena Galwa
# 08/05/2025
# Description:
#   Python for Data Quality Engineers [SELF-PACED 2025] - Home Task 1
#   Create a python script:
#       1. Create a list of 100 random numbers from 0 to 1000.
#       2. Sort list from min to max using a Bubble Sort algorithm (no sort()).
#       3. Calculate average for even and odd numbers.
#       4. Print both average results to console.
#       5. Commit the script to a git repository and provide the link as the home task result.

# Importing random module
import random

# Define total number of elements in list
n = 100

# Define list and assign random numbers to i
random_list = random.sample(range(0, 1000), n)

# Print initial random list to check the content
print("Initial list:", random_list)

# Full Bubble Sort implementation
for i in range(n):
    swapped = False  # Track if a swap occurred
    for j in range(0, n - i - 1):
        if random_list[j] > random_list[j + 1]:
            random_list[j], random_list[j + 1] = random_list[j + 1], random_list[j]
            swapped = True
    if not swapped:  # If no swap occurred, the list is sorted
        break

# Print fully sorted list
print("\n\nFully sorted list:", random_list)

# Initiate counter variables and sum variables for checking Even and Odd numbers
SumEvenNumbers = 0
CounterEvenNumbers = 0
SumOddNumbers = 0
CounterOddNumbers = 0

# Check Even and Odd numbers
for i in range(n):
    if random_list[i] % 2 == 0:
        CounterEvenNumbers += 1
        SumEvenNumbers += random_list[i]
    else:
        CounterOddNumbers += 1
        SumOddNumbers += random_list[i]

# Calculate average values for Even and Odd numebrs
AverageEven = SumEvenNumbers / CounterEvenNumbers
AverageOdd = SumOddNumbers / CounterOddNumbers

# Print average values for Even numbers and Odd numbers
print("\n\nAverage value of Even numbers:", AverageEven, "\n\nAverage value of Odd numbers:", AverageOdd,  )


