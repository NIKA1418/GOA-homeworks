def sum_positive_numbers(numbers):
    return sum(num for num in numbers if num > 0)

# Example usage
numbers = [1, -4, 7, 12]
result = sum_positive_numbers(numbers)
print(result)  # Output: 20

def repeat_string(n, s):
    return s * n

# Example usage
print(repeat_string(6, "I"))      # Output: IIIIII
print(repeat_string(5, "Hello"))  # Output: HelloHelloHelloHelloHello

def remove_first_last(s):
    return s[1:-1]

# Example usage
print(remove_first_last("Hello"))  # Output: "ell"
print(remove_first_last("Python")) # Output: "ytho"
print(remove_first_last("AB"))     # Output: "" (Empty string)

def square_sum(numbers):
    return sum(num ** 2 for num in numbers)

# Example usage
print(square_sum([1, 2, 2]))  # Output: 9
print(square_sum([3, 4, 5]))  # Output: 50
print(square_sum([0, -1, -2]))  # Output: 5

def find_smallest_integer(numbers): return min(numbers)
Example usage
print(find_smallest_integer([34, 15, 88, 2]))  # Output: 2 print(find_smallest_integer([34, -345, -1, 100]))  # Output: -345

