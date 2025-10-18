students = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "C",
    "David": "A",
    "Eve": "B"
}

print("Students and their grades:")
for name, grade in students.items():
    print(f"{name}: {grade}")

countries = {
    "France": "Paris",
    "Japan": "Tokyo",
    "Germany": "Berlin",
    "Canada": "Ottawa",
    "Brazil": "Brasília"
}

print("Capitals of the listed countries:")
for capital in countries.values():
    print(capital)

cars = {
    "Toyota": "Supra",
    "Ford": "Mustang",
    "Tesla": "Model S",
    "BMW": "M3",
    "Mercedes": "AMG GT"
}

# Displaying a favorite car model
favorite_car = cars["Tesla"]
print(f"My favorite car model is: {favorite_car}")

book = {
    "Title": "1984",
    "Author": "George Orwell",
    "Year": 1949,
    "Genre": "Dystopian"
}

# Updating the year of publication
book["Year"] = 1950

print("Updated book information:")
print(book)

students_points = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 92,
    "Eve": 88
}

average_points = sum(students_points.values()) / len(students_points)
print(f"The average student points: {average_points}")

user_info = {}

user_info["Name"] = input("Enter your name: ")
user_info["Surname"] = input("Enter your surname: ")
user_info["Age"] = int(input("Enter your age: "))
user_info["Height"] = float(input("Enter your height in cm: "))
user_info["Career"] = input("Enter your career: ")

print("User information stored in dictionary:")
print(user_info)

