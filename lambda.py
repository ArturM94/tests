"""Zeros and ones with lambda"""

indexes = range(10)

lambda_mapped_array = list(map(lambda index: 0 if index % 2 == 0 else 1, indexes))
print(lambda_mapped_array)

lambda_list_comprehension_array = [(lambda index: 0 if index % 2 == 0 else 1)(index) for index in indexes]
print(lambda_list_comprehension_array)

# bad way (PEP 8)
lambda_array = lambda indexes: [0 if index % 2 == 0 else 1 for index in indexes]
print(lambda_array(indexes))

lambda_cycled_array = []
for index in indexes:
    lambda_cycled_array.append((lambda index: 0 if index % 2 == 0 else 1)(index))
print(lambda_cycled_array)
