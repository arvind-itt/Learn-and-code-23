iteration_count = 0

def count_unique_digits(number):
    unique_digits = set(number)
    return len(unique_digits) >= 2

def bubble_sort_ascending(string):
    # Custom Bubble Sort implementation for sorting in ascending order
    size = len(string)
    for current_index in range(size):
        for next_index in range(0, size - current_index - 1):
            if string[next_index] > string[next_index + 1]:
                string[next_index], string[next_index + 1] = string[next_index + 1], string[next_index]
    return string

def bubble_sort_descending(string):
    # Custom Bubble Sort implementation for sorting in descending order
    size = len(string)
    for current_index in range(size):
        for next_index in range(0, size - current_index - 1):
            if string[next_index] < string[next_index + 1]:
                string[next_index], string[next_index + 1] = string[next_index + 1], string[next_index]
    return string

def string_to_integer(string):
    # Custom implementation for converting string to integer
    result = 0
    for char in string:
        result = result * 10 + (ord(char) - ord('0'))
    return result

def find_kaprekar_iterations(number):
    global iteration_count

    # Base cases when length is more
    # than 4 or number does not have
    # at least two distinct digits
    if (not count_unique_digits(number) or len(number) > 4) and iteration_count == 0:
        return -1
    elif int(number) == 6174:
        return iteration_count

    # Count iterations
    iteration_count += 1

    # If input string has less than 4
    # characters, insert '0' at the front
    while len(number) < 4:
        number = "0" + number

    original_number = list(number)

    # Sorting in ascending and descending
    # order based on ASCII value
    sorted_number = bubble_sort_ascending(list(number))
    reversed_sorted_number = bubble_sort_descending(original_number)

    # Conversion from string to integer
    highestNumber = string_to_integer(''.join(sorted_number))
    lowestNumber = string_to_integer(''.join(reversed_sorted_number))

    # Final calculation of bigger-smaller
    # number
    result_string = str(abs(highestNumber - lowestNumber))

    # If 6174 is not reached yet,
    # then recur with the updated string
    return find_kaprekar_iterations(result_string)

# Driver's code
if __name__ == "__main__":
    number = input("Enter Number: ")

    # Function call
    result = find_kaprekar_iterations(number)

    if result != -1:
        print(f"Number of iterations to reach 6174: {result}")
    else:
        print("Invalid input.")
