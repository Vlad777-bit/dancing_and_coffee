list_of_products = [["milk", 0, 0],["bread", 0, 0],["cake", 0, 0]]

for item in list_of_products:
  item[1] = int(input(f"Введите стоимость {item[0]} в магазине пятерочка "))
  item[2] = int(input(f"Введите стоимость {item[0]} в магазине магнит "))

pyaterochka_sum = sum([sublist[1] for sublist in list_of_products])
print(f"сумма покупок в магазине пятерочка составляет {pyaterochka_sum}")

magnit_sum = sum([sublist[2] for sublist in list_of_products])
print(f"сумма покупок в магазине магнит составляет    {magnit_sum}")

if pyaterochka_sum > magnit_sum:
  print(f"совершив покупки в магните, вы сэкономите {pyaterochka_sum - magnit_sum}")
elif pyaterochka_sum < magnit_sum:
  print(f"совершив покупки в пятерочке, вы сэкономите {magnit_sum - pyaterochka_sum}")
else:
  print("стоимость покупок в пяторочке и магните одинакова")

