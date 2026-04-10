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

def third_highest(array):
    third_array = sorted(set(array), reverse=True)[2]
    print (third_array)
    return third_array

my_numbers = [10, 15, 1, 300, 400, 200, 500, 1000]
third_highest = third_highest(my_numbers)
print(third_highest)