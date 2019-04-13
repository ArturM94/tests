"""Zeros and ones with lambda"""

indexes = range(10)

lambda_mapped_array = list(map(lambda index: 0 if index % 2 == 0 else 1, indexes))
print(lambda_mapped_array)

lambda_list_comprehension_array = [(lambda index: 0 if index % 2 == 0 else 1)(index) for index in indexes]
print(lambda_list_comprehension_array)
