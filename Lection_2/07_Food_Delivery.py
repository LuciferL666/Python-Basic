chiken_menues_amount = int(input()) * 10.35
fish_menues_amount = int(input()) * 12.40
vegetarian_menues_amount = int(input()) * 8.15
total_menues_money = chiken_menues_amount + fish_menues_amount + vegetarian_menues_amount
dessert_price = total_menues_money * 0.2
delivery = 2.50
total_price = total_menues_money + dessert_price + delivery
print(total_price)