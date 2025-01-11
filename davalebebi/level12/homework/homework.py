age = int(input("გთხოვთ, შეიყვანეთ თქვენი ასაკი: "))
future_age = age + 10
print(f"10 წელში თქვენ იქნებით {future_age} წლის.")













num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2
div_result = num1 / num2 if num2 != 0 else "განაყოფი ვერ გამოითვლება (ნული ვერ იქნება გამყოფი)"

print("ჯამი:", sum_result)
print("სხვაობა:", diff_result)
print("ნამრავლი:", prod_result)
print("განაყოფი:", div_result)












age = int(input("გთხოვთ, შეიყვანეთ თქვენი ასაკი: "))
past_age = age - 10
print(f"10 წელში თქვენ იქნებით {past_age} წლის.")
