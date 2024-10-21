def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Funtion in use
input_list = [10, 20, 5, 40, 30]
largest_number = find_largest(input_list)
print(largest_number)
