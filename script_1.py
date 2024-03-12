num_tickets = int(input("Введите количество билетов: "))
c= 0
total_c = 0

for i in range(num_tickets):
    age = int(input(f"Введите возраст {i + 1}: "))
    if age < 18:
        c = 0
    elif 18 <= age < 25:
        c = 990
    else:
        c = 1390
    total_c += c

if num_tickets > 3:
    total_c *= 0.9  

print(f"Общая стоимость: {total_c}")
