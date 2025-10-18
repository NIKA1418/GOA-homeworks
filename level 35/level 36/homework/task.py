sentence = "Learning Python is fun!"
position = sentence.find("Python")
print(f"The position of 'Python' is: {position}")

string = input("Enter a string: ")
substring = input("Enter the substring to search for: ")
index = string.find(substring)
print(f"The starting index of '{substring}' is: {index}")

def find_char_index(string, char):
    return string.find(char)

string = "hello world"
char = "o"
print(f"The index of '{char}' is: {find_char_index(string, char)}")

paragraph = "The quick brown fox jumps over the lazy dog. The dog barked."
count = paragraph.lower().count("the")
print(f"The word 'the' appears {count} times.")

string = input("Enter a string: ")
char = input("Enter a character to count: ")
count = string.count(char)
print(f"The character '{char}' appears {count} times.")

def count_word(text, word):
    return text.lower().count(word.lower())

text = "This is a test. This is only a test."
word = "test"
print(f"The word '{word}' appears {count_word(text, word)} times.")

string = "hello world, hello Python!"
index = string.find("hello")
print(f"The first occurrence of 'hello' is at index: {index}")

def find_index(string, char):
    return string.find(char)

string = "programming"
char = input("Enter a character: ")
print(f"The index of '{char}' is: {find_index(string, char)}")

string = "hello world"
print(string.islower())

def is_all_lowercase(string):
    return string.islower()

string = "hello world"
print(is_all_lowercase(string))

string = input("Enter a string: ")
if string.islower():
    print("The string contains only lowercase letters.")
else:
    print("The string contains characters that are not lowercase.")