basic_salary = 1500
bonus = 200
commission_rate = 0.02
number_of_laptop = int(input("enter_number_of_laptops"))
price =float(input("enter_price_of_laptops"))

bonus = (bonus * number_of_laptop)

commision_rate = (commission_rate * number_of_laptop *
price)

Gross_salary=basic_salary + bonus + commision_rate

print(Gross_salary)

print(bonus)

print(commision_rate)

print(Gross_salary+bonus+commision_rate)

