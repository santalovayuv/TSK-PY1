list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_number = list_numbers[0]
for current_number in list_numbers:
    if current_number > max_number:
        max_number = current_number
index = list_numbers.index(max_number)
list_numbers[-1], list_numbers[index] = list_numbers[index], list_numbers[-1]
print(list_numbers)
