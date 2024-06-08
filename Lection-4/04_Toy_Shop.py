PUZZEL_PRICE = 2.60
TALKING_DOLLS_PRICE = 3
TADDY_BEARS_PRICE = 4.10
MINIONS_PRICE = 8.20
TRUCKS_PRICE = 2

vacantion_price = float(input())
puzzel_amount = int(input())
taking_dolls_amount = int(input())
taddy_bears_amount = int(input())
minions_amount = int(input())
trucks_amount = int(input())

total_price = (
puzzel_amount * PUZZEL_PRICE +
taking_dolls_amount * TALKING_DOLLS_PRICE +
taddy_bears_amount * TADDY_BEARS_PRICE +
minions_amount * MINIONS_PRICE +
trucks_amount * TRUCKS_PRICE
)
total_amount_toys = (
puzzel_amount +
taking_dolls_amount +
taddy_bears_amount +
minions_amount +
trucks_amount
)

if total_amount_toys >= 50:
    total_price *= 0.75

total_price *= 0.90

if total_price >= vacantion_price:
    print(f"Yes! {total_price - vacantion_price:.2f} lv left.")
else:
    print(f"Not enough money! {vacantion_price - total_price:.2f} lv needed.")


