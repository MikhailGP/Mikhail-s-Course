per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

TKB = per_cent['ТКБ']
CKB = per_cent['СКБ']
VTB = per_cent['ВТБ']
CBER = per_cent['СБЕР']

money = float(input("Введите планируемую сумму вклада - "))

deposit = [money * TKB * 0.01, money * CKB * 0.01, money * VTB * 0.01, money * CBER * 0.01]

max_deposit = max(deposit)

deposit = str(deposit)

max_deposit = str(max_deposit)

print("Накопленные средства за год в каждом из банков: " + deposit)

print("Максимальная сумма которую вы можете заработать - " + max_deposit + " рублей")