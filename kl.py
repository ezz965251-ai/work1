def remove_number_from_list(numbers, number_to_remove):
    removed_count = 0
    new_list = []
    for num in numbers:
        if num != number_to_remove:
            new_list.append(num)
        else:
            removed_count += 1
    numbers.clear()
    for num in new_list:
        numbers.append(num)
    return removed_count
list1 = [1, 2, 3, 2, 4, 2, 5]
number1 = 2
print(f"Исходный список: {list1}")
print("Число для удаления: {number1}")