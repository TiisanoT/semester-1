# Worksheet 1.2: Task 2 Solution

import sys
from util import read_numbers

numbers = read_numbers()



if not numbers:
    sys.exit("Erorr: no numebrs provided")

minimum = min(numbers)
maximum = max(numbers)
mean = sum(numbers) / len(numbers)
 
numbers.sort()
size = len(numbers)

if size % 2 == 1:
    median = numbers[size // 2]
else:
    middle = size // 2
    median = (numbers[middle - 1] + numbers[middle]) / 2
        
        
print("Minimum =", minimum)
print("Maximum =", maximum)
print("Mean =", mean)
print("Median =", median)

   

