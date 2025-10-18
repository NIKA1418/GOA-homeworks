def say_hello():
    print("Hello, World!")

say_hello()

def add_numbers(a, b):
    print(a + b)

add_numbers(5, 3)  # Outputs 8
def multiply_by_ten(num):
    return num * 10

result = multiply_by_ten(4)
print(result)  # Outputs 40
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()          # Outputs "Hello, Guest!"
greet("Nika")   # Outputs "Hello, Nika!"

def outer_function():
    def inner_function():
        print("Inner function called!")

    inner_function()

outer_function()

def check_even_odd(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is Odd")

check_even_odd([1, 2, 3, 4, 5, 6])

def find_maximum(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(find_maximum([3, 5, 1, 9, 2]))

def filter_positive(numbers):
    return [num for num in numbers if num > 0]

print(filter_positive([-2, 5, -8, 3, 0, 9]))

def sum_divisible_by_three():
    return sum(num for num in range(1, 101) if num % 3 == 0)

print(sum_divisible_by_three())

