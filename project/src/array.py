numbers = [10, 5, 6, 1, 0]
smallest = numbers[0]
lowest_number = min(numbers)
print(lowest_number)

for number in numbers:
    if number == lowest_number:
        print(lowest_number);

for number in numbers:
    if number < smallest:
        smallest = number
print(smallest)


def find_second_highest(num):
    unique_arr = list(set(num))
    if len(unique_arr) < 2:
        return None
    unique_arr.sort(reverse=True)
    return unique_arr[1]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
second_highest = find_second_highest(my_list)
print(second_highest)

def third_highest(num):
    third_array = sorted(set(num), reverse=True)[2]
    return third_array

my_numbers = [10, 15, 1, 300, 400, 200, 500, 1000]
third_highest = third_highest(my_numbers)
print(third_highest)

# duplicate array

def has_duplicate(arr):
    return len(arr) != len(set(arr))

print(has_duplicate([1, 4, 5, 5, 6]))