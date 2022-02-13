tickets = int(input("Какое количество билетов вы бы хотели купить? "))
price = []
print("необходимое количество билетов - ", tickets)
for i in range(1, tickets + 1):
    age = int(input(f"Введите возраст {i} посетителя - "))
    if 0 < age < 18:
        price.append(0)
    elif 18 <= age < 25:
        price.append(990)
    elif age >= 25:
        price.append(1390)
    elif age < 0:
        print(f"Возраст не может быть меньше 0! Расчет цены может быть некорректен!")
print("Итого стоимость билетов составит - ", sum(price))
if tickets > 3:
   final_price = int(sum(price) * 0.9)
   print("Сумма к оплате с учетом скидки за количество больше 3-х - ", final_price)
else:
   final_price = sum(price)
   print("Сумма к оплате ", final_price)
