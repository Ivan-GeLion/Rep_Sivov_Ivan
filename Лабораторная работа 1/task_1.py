numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

none_type_in_numbers = 4
skip_none = numbers[:none_type_in_numbers] + numbers[none_type_in_numbers+1:]
sum_numbers = sum(skip_none)
count_numbers = len(numbers)
average = sum_numbers / count_numbers
numbers[none_type_in_numbers] = average
print("Измененный список:", numbers)
