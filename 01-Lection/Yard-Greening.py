k_metars = float(input())
price_for_one_Kmetar = 7.61
price_without_discount = k_metars * price_for_one_Kmetar
discount = 0.18
discount_money = price_without_discount * discount
final_price = price_without_discount - discount_money
print(f'The final price is: {final_price} lv.')
print(f"The discount is: {discount_money} lv.")