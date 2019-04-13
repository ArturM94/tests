"""Zeros and ones with lambda"""

indexes = range(10)

lambda_mapped_array = list(map(lambda x: 0 if x % 2 == 0 else 1, indexes))
print(lambda_mapped_array)
