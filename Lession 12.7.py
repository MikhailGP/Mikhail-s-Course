per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

TKB = per_cent['ТКБ']
CKB = per_cent['СКБ']
VTB = per_cent['ВТБ']
CBER = per_cent['СБЕР']
#Наверняка это можно было сделать как-то иначе, проще. Пока не придумал как

money = float(input("Введите планируемую сумму вклада - "))

deposit_TKB = money * TKB * 0.01
deposit_CKB = money * CKB * 0.01
deposit_VTB = money * VTB * 0.01
deposit_CBER = money * CBER * 0.01
#Наверняка это можно было сделать как-то иначе, проще. Пока не придумал как

deposit_all = [deposit_TKB, deposit_CKB, deposit_VTB, deposit_CBER]

max_deposit = max(deposit_all)

deposit_all = str(deposit_all)
max_deposit = str(max_deposit)
deposit_TKB = str(deposit_TKB)
deposit_CKB = str(deposit_CKB)
deposit_VTB = str(deposit_VTB)
deposit_CBER = str(deposit_CBER)
#Наверняка это можно сделать одной командой, пока не понял как

print("Накопленные средства за год в каждом из банков: " + deposit_all)
#Вывод результата одним списком

print("Накопленные средства за год в банке ТКБ: " + deposit_TKB)
print("Накопленные средства за год в банке СКБ: " + deposit_CKB)
print("Накопленные средства за год в банке ВТБ: " + deposit_VTB)
print("Накопленные средства за год в банке СБЕР: " + deposit_CBER)
#Вывод результата отдельно для каждого из банков

print("Максимальная сумма которую вы можете заработать - " + max_deposit)