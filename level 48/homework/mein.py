1
def past(h, m, s):
    return (h * 3600 + m * 60 + s) * 1000

2
def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'
3
def simple_multiplication(number):
    return number * 8 if number % 2 == 0 else number * 9

4
def abbrev_name(name):
    return '.'.join([word[0].upper() for word in name.split()])

5
def find_needle(haystack):
    return f"found the needle at position {haystack.index('needle')}"

6
def invert(lst):
    return [-x for x in lst]

7
def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

8
def smash(words):
    return ' '.join(words)

9
from functools import reduce

def grow(arr):
    return reduce(lambda x, y: x * y, arr)

10
def hero(bullets, dragons):
    return bullets >= dragons * 2

1
def better_than_average(class_points, your_points):
    return your_points > (sum(class_points) / len(class_points))

2
def count_positives_sum_negatives(arr):
    if not arr:
        return []
    count_positives = sum(1 for x in arr if x > 0)
    sum_negatives = sum(x for x in arr if x < 0)
    return [count_positives, sum_negatives]

3
def dna_to_rna(dna):
    return dna.replace('T', 'U')

4
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left

5
def bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    else:
        return "Obese"
    