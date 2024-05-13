deposit_amount = float(input())
months_deposit = int(input())
annual_interest_rate = float(input())
interest = deposit_amount * annual_interest_rate / 100
month_interest = interest / 12
total = deposit_amount + months_deposit * month_interest
print(total)