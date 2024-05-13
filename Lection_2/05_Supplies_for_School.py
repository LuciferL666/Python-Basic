PRICE_PENS = 5.80
PRICE_MARKERS = 7.20
PRICE_CLEANER = 1.20

amount_pens = int(input())
amount_markers = int(input())
liter_cleaner = int(input())
discount = int(input())

pens_total = amount_pens * PRICE_PENS
markers_total = amount_markers * PRICE_MARKERS
cleaner_total = liter_cleaner * PRICE_CLEANER
discount_amount = discount / 100
total = pens_total + markers_total + cleaner_total
price_with_discount = total - (total * discount_amount)
print(price_with_discount)
