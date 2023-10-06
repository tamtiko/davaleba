def find_min_value(dictionary):
    min_value = float('inf')

    for value in dictionary.values():
        if isinstance(value, int):
            min_value = min(min_value, value)
    
    if min_value == float('inf'):
        return None  
    else:
        return min_value

my_dictionary = {'a': 51, 'b': 200, 'c': 2, 'd': 555, 'e': 777777}
result = find_min_value(my_dictionary)
print(result)
