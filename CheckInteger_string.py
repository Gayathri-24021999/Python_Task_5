# Sample list
elements = [1, 'hello', 3.14, 42, 'world', '123', 7]

# Use lambda function to check if each element is an integer or string
check_types = list(map(lambda x: 'Integer' if isinstance(x, int) else 'String' if isinstance(x, str) else 'Other', elements))

# Print the results
for element, result in zip(elements, check_types):
    print(f"{element}: {result}")
