names = ["Ali", "Bob", "Ana", "Charlie", "David", "Elo", "Andrew", "Diana", "George", "Erakle"]

# renewed სიის შესაქმნელად ვუყენებთ list comprehension ს
renewed = [name for name in names if len(name) < 6 or name.startswith("A")]

# შედეგის ჩვენება
print(renewed)
