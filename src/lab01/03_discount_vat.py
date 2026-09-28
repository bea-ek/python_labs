price = float(input("price: ").replace(',','.'))
discount = float(input("discount: ").replace(',','.'))
vat = float(input('vat: ').replace(',','.'))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f'База после скидки: {base:>10.2f} ₽')
print(f'НДС: {vat_amount:>24.2f} ₽')
print(f'База после скидки: {total:>10.2f} ₽')
