name1 = input("Product 1: ")
qty1 = int(input("Quantity: "))
price1 = float(input("Unit price: "))

name2 = input("Product 2: ")
qty2 = int(input("Quantity: "))
price2 = float(input("Unit price: "))

name3 = input("Product 3: ")
qty3 = int(input("Quantity: "))
price3 = float(input("Unit price: "))

total1 = qty1 * price1
total2 = qty2 * price2
total3 = qty3 * price3

subtotal = total1 + total2 + total3
vat = subtotal * 0.19
total = subtotal + vat

print(f"{'Product':<12}{'Qty':>5}{'Unit':>8}{'Line total':>14}")
print(f"{name1:<12}{qty1:>5}{price1:>8.2f}{total1:>14.2f}")
print(f"{name2:<12}{qty2:>5}{price2:>8.2f}{total2:>14.2f}")
print(f"{name3:<12}{qty3:>5}{price3:>8.2f}{total3:>14.2f}")
print("-" * 39)
print(f"{'Subtotal':<25}{subtotal:>14.2f}")
print(f"{'VAT (19%)':<25}{vat:>14.2f}")
print(f"{'Total':<25}{total:>14.2f}")