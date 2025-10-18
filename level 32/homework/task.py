def sum_numbers(a, b):
    sum = a + b
    print("ჯამი:", sum)

# Function Call Example
sum_numbers(5, 7)  # Output: ჯამი: 12

def reverse_string(s):
    return s[::-1]

# Function Call Example
result = reverse_string("nika")
print("Reversed string:", result)  # Output: Reversed string: akin

def find_maximum(numbers):
    return max(numbers)

# Function Call Example
result = find_maximum([3, 9, 1, 7])
print("Maximum value:", result)  # Output: Maximum value: 9


#ფუნქცია არის კოდის ნაწყვეტი, რომელიც ასრულებს კონკრეტულ დავალებას. ფუნქციების გამოყენება ჯობია, რადგან:
# თავიდან გვაცილებს კოდის გამეორებას.
# ზრდის კოდის გასაგებადობას და სიმარტივეს.
# ქმნის მოქნილობას, რადგან მონაცემები შეიძლება სხვადასხვანაირად მიეწოდოს.


def my_function():
    print("Hello!")


def greet():  # `greet` აქ ფუნქციის სახელია.
    print("გამარჯობა!")


def greet(name):  # `name` პარამეტრია.
    print("გამარჯობა,", name)

def say_hello():
    print("Indented code here")  # Indented code

    
    print("Line 1")
    print("Line 2")  # ეს ორი ხაზი კოდის ბლოკია.

greet("ნიკა")  # ფუნქციის გამოძახება.

def add(a, b):
    return a + b

print(add(5, 10))  # აქ 5 და 10 არგუმენტებია.
