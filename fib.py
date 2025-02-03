# Function to return the nth Fibonacci number
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# Example: Get the 10th Fibonacci number
print(fib(10))

