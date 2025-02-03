# Fibonacci Recursive Solution
This repository contains a simple implementation of calculating Fibonacci numbers using a recursive approach.

# Overview
The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. 
The recursive solution provided in this repository calls the function on smaller subproblems to compute the Fibonacci number at position n.

# Recursive Approach
The main function calls itself to find the previous two Fibonacci numbers, adds them together, and returns the result for the given position n. 
The base cases are:

-Fibonacci(0) = 0

-Fibonacci(1) = 1

For values of n > 1, the function recursively calls Fibonacci(n-1) and Fibonacci(n-2) and adds their results.

```
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```
# Performance Note
For larger values of n, this recursive approach can become inefficient because it involves a lot of repeated calculations (i.e., the same Fibonacci numbers are recalculated multiple times). The time complexity of this approach is exponential, specifically O(2^n).

# Optimizing for Larger n
For larger values of n, an iterative approach or memoization would be much more efficient:

Iterative approach has O(n) time complexity and O(1) space complexity.
Memoization stores previously computed Fibonacci numbers to avoid redundant calculations.

Example

# Calculate the 6th Fibonacci number
```
result = fibonacci(6)
print(result)  # Output: 8

```

# Contributions
Feel free to fork the repository and submit issues or pull requests for improvements, optimizations, or additional features!

# License
This project is licensed under the MIT License - see the LICENSE file for details.
