words = ["hello", "world", "python"]
uppercase_words = list(map(str.upper, words))

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))

numbers = [10, 20, 30, 40]
incremented_numbers = list(map(lambda x: x + 5, numbers))

celsius_temps = [0, 20, 30, 40]
fahrenheit_temps = list(map(lambda c: (c * 9/5) + 32, celsius_temps))

words = ["apple", "banana", "cherry"]
first_chars = list(map(lambda x: x[0], words))

numbers = [1, 2, 3, 4, 5, 6]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

words = ["apple", "banana", "kiwi", "strawberry"]
long_words = list(filter(lambda x: len(x) > 5, words))

numbers = [-10, 20, -5, 30, -1]
positive_numbers = list(filter(lambda x: x >= 0, numbers))

names = ["Alice", "Bob", "Angela", "Charlie"]
a_names = list(filter(lambda x: x.startswith("A"), names))

numbers = [3, 5, 9, 12, 14, 18]
divisible_by_3 = list(filter(lambda x: x % 3 == 0, numbers))

