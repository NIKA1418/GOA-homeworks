# Example list and string
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_string = "HelloWorld"

# 2) Get the first five elements from a list
first_five_elements = my_list[:5]

# 3) Get the last three characters from a string
last_three_characters = my_string[-3:]

# 4) Get every second element from a list starting from the beginning
every_second_element = my_list[::2]

# 5) Get every third element from a list
every_third_element = my_list[::3]

# 6) Use negative indexing to get the last element of a list
last_element = my_list[-1]

# 7) Get a slice of a string excluding the first and last character
string_slice = my_string[1:-1]

# 8) Get a slice of a list from the middle to the end
middle_to_end = my_list[len(my_list)//2:]

# 9) Use slicing to get a copy of a list
copy_of_list = my_list[:]

# 10) Get a reversed string using slicing
reversed_string = my_string[::-1]

# 11) Get the first half of a list
first_half = my_list[:len(my_list)//2]

# 12) Use slicing to get the list excluding the first three elements
exclude_first_three = my_list[3:]

# 13) Get a portion of a string using both positive and negative indices
portion_of_string = my_string[2:-2]

# 14) Get the last five elements from a list
last_five_elements = my_list[-5:]
