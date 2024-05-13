kvm_nylon = int(input()) + 2
liter_paint = int(input())
paint_thinner = int(input())
work_hours = int(input())
bags = 0.4
nylon_price = 1.50
price_paint_liter = 14.50
paint_thinner_price = 5
total_nylon_price = kvm_nylon * nylon_price
total_paint = liter_paint * 0.1
total_paint_price = (total_paint + liter_paint) * price_paint_liter
total_price_paint_thinner = paint_thinner * paint_thinner_price
total_money_for_materials = total_paint_price + total_price_paint_thinner + total_nylon_price + bags
money_for_workers = (total_money_for_materials * 0.3) * 8
total_price_all = total_money_for_materials + money_for_workers
print(total_price_all)