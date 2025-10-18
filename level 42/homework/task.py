def sum_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)

# ტესტირება
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_even_numbers(numbers_list))  # → 30

def square_sum_odd_numbers(numbers):
    return sum(num for num in numbers if num % 2 != 0) ** 2

# ტესტირება
print(square_sum_odd_numbers(numbers_list))  # → 225

def process_even_odd(numbers):
    even_arr = [num for num in numbers if num % 2 == 0]
    odd_arr = [num for num in numbers if num % 2 != 0]
    
    return sum(even_arr) * sum(odd_arr)

# ტესტირება
print(process_even_odd(numbers_list))  # → 6750

