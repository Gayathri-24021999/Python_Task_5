# Fibonacci series
# Using reduce to generate Fibonacci series up to n elements
from functools import reduce
fibonacci_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n-2), [0, 1])

# Get first 50 elements
fib_series = fibonacci_series(50)

print(fib_series)
