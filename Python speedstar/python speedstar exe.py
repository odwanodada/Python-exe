average_speed = float(input("enter_average_speed"))
current_speed = float(input("enter_your_current_speed"))

if (current_speed<average_speed):
    print("OK")

elif current_speed > average_speed:
    point = 0
while current_speed>average_speed:
    point+= 1
    current_speed-=5
    print(point)
if point>2:
    print("Time to go to jail")
