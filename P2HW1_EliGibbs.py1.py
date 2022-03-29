# Products with their designated prices
# 3/28/22
# CTI-110 P2HW1 - Total Purchases
# Eli Gibbs
#

SALES_TAX = .07

Toothpaste = float(input('\nEnter the price for item 1 $'))56.75
Toothbrush = float(input('Enter the price for item 2 $'))17.55
SilverWare = float(input('Enter the price for item 3 $')) 45
Phone Charger = float(input('Enter the price for item 4 $'))89.99
Bread Sticks = float(input('Enter the price for item 5 $'))90

subtotal =  float(item1 + item2 + item3 + \
                  item4 + item5)

total_sales_tax = subtotal * SALES_TAX

total = subtotal + total_sales_tax
#3,000,000.09
print('\nTotal = $', format(total, ',.2f'), sep='', end='\n\n')
