# 2) გადაიყვანე წინადადება uppercase ფორმატში და დაბეჭდე ამ სახით
sentence = input("Enter a sentence: ")
print(sentence.upper())

# 3) მომხმარებელს შემოატანინე სახელი და დაუბეჭდე uppercase ფორმატში
name = input("Enter your name: ")
print(name.upper())

# 4) შექმენი ფუნქცია, რომელსაც გადაეცემა სთრინგების სია. ფუნქციამ სთრინგის თითოეული სთრინგი უნდა დაბეჭდოს uppercase ფორმატში
def print_uppercase(strings):
    for s in strings:
        print(s.upper())

string_list = ["hello", "world", "python"]
print_uppercase(string_list)


# 5) გადაიყვანე წინადადება lowercase ფორმატში და დაბეჭდე ამ სახით
sentence = input("Enter a sentence: ")
print(sentence.lower())

# 6) მომხმარებელს შემოატანინე მეილი და დაუბეჭდე lowercase ფორმატში
email = input("Enter your email: ")
print(email.lower())

# 7) შექმენი ფუნქცია, რომელიც მიიღებს სთრინგს და გადაიყვანს მას lowercase ფორმატში, დაბეჭდავს ამ სახით
def print_lowercase(string):
    print(string.lower())

sample_string = "HELLO PYTHON"
print_lowercase(sample_string)


# 5) გადაიყვანე წინადადება lowercase ფორმატში და დაბეჭდე ამ სახით
sentence = input("Enter a sentence: ")
print(sentence.lower())

# 6) მომხმარებელს შემოატანინე მეილი და დაუბეჭდე lowercase ფორმატში
email = input("Enter your email: ")
print(email.lower())

# 7) შექმენი ფუნქცია, რომელიც მიიღებს სთრინგს და გადაიყვანს მას lowercase ფორმატში, დაბეჭდავს ამ სახით
def print_lowercase(string):
    print(string.lower())

sample_string = "HELLO PYTHON"
print_lowercase(sample_string)
