#Making A Vending Machine


print('''___𝑾𝑬𝑳𝑪𝑶𝑴𝑬 𝑻𝑶 𝑻𝑯𝑬 𝑴𝑶𝑯𝑫 𝑨𝑫𝑰𝑳 𝑯𝑶𝑺𝑺𝑨𝑰𝑵 𝑽𝑬𝑵𝑫𝑰𝑵𝑮 𝑴𝑨𝑪𝑯𝑰𝑵𝑬___''')

print("___𝑾𝑬𝑳𝑪𝑶𝑴𝑬 𝑻𝑶 𝑻𝑯𝑬 𝑴𝑬𝑵𝑼!!___")

print("___𝑯𝑶𝑾 𝑪𝑨𝑵 𝑰 𝑯𝑬𝑳𝑷 𝒀𝑶𝑼___")


#Menu Book
print("______________𝓜𝓔𝓝𝓤 𝓑𝓞𝓞𝓚________________")
print("____𝓓𝓡𝓘𝓝𝓚𝓢_______________________________")
print("A1.                COKE              2.50DHS")
print("A2.                PEPSI             2.50DHS")
print("B1.                WATER             1.50DHS")
print("B2.               COFFEE            12.50DHS")
print("C1.         ORANGE JUICE             7.50DHS")
print("C2.            MILKSHAKE             5.25DHS")
print("____𝓢𝓝𝓐𝓒𝓚𝓢_______________________________")
print("D1.              POPCORN             2.50DHS")
print("D2.              BISCUITS            8.00DHS")
print("E1.               CHIPS              4.25DHS")
print("E2.              MIXNUTS             7.25DHS")
print("F1.           CHOCOLATE BAR          4.25DHS")
print("F2.            PROTEIN BAR          25.50DHS")

#Items
MENU_BOOK = {
'A1': {'NAME': 'COKE', 'price': 2.50},
'A2': {'NAME': 'PEPSI', 'price': 2.50},
'B1': {'NAME': 'WATER', 'price': 1.50},
'B2': {'NAME': 'COFFEE', 'price': 12.50},
'C1': {'NAME': 'ORANGE JUICE', 'price': 7.50},
'C2': {'NAME': 'MILKSHAKE', 'price': 5.25},
'D1': {'NAME': 'POPCORN', 'price': 2.50},
'D2': {'NAME': 'BISCUITS', 'price': 8.00},
'E1': {'NAME': 'CHIPS', 'price': 4.25},
'E2': {'NAME': 'MIXNUTS', 'price': 7.25},
'F1': {'NAME': 'CHOCOLATE BAR', 'price': 4.25},
'F2': {'NAME': 'PROTEIN BAR', 'price': 25.50}
}

#Enter the code for which items you want.
MENU=input('ENTER THE CODE OF THE ITEMS FOR PURCHASE:')
if MENU in MENU_BOOK:
    ITEM = MENU_BOOK[MENU]
    PRICE = ITEM['price']

#Insert The Money.
MONEY=float(input("ENTER THE MONEY YOU WANT TO INSERT:"))
CHANGE= MONEY-PRICE

#The choice Of Items.
choice=input('WOULD YOU LIKE SOMETIME (YES/NO):')
if choice== 'YES':
   print("____________________________________")
   print("THANK YOU FOR THE SELECTING THE ITEM")
elif choice== 'NO':
   print("____________________________________")
   print("THANK YOU AND HAVE A NICE DAY")

#Calculte & Return the Money for items
if MENU=='A1':
         print("-------------------------------")
         print("YOUR CHANGE IS",CHANGE)
         print("YOUR ORDER HAS BEEN PROVIDED")
         print("TAKE YOUR BILLS OR RECEIPIT")
         print("THANK YOU AND HAVE A GREAT DAY")
         print("-------------------------------")

if MENU=='A2':
         print("-------------------------------")
         print("YOUR CHANGE IS",CHANGE)
         print("YOUR ORDER HAS BEEN PROVIDED")
         print("TAKE YOUR BILLS OR RECEIPIT")
         print("THANK YOU AND HAVE A GREAT DAY")
         print("-------------------------------")

if MENU=='B1':
         print("-------------------------------")
         print("YOUR CHANGE IS",CHANGE)
         print("YOUR ORDER HAS BEEN PROVIDED")
         print("TAKE YOUR BILLS OR RECEIPIT")
         print("THANK YOU AND HAVE A GREAT DAY")
         print("-------------------------------")

if MENU=='B2':
         print("-------------------------------")
         print("YOUR CHANGE IS",CHANGE)
         print("YOUR ORDER HAS BEEN PROVIDED")
         print("TAKE YOUR BILLS OR RECEIPIT")
         print("THANK YOU AND HAVE A GREAT DAY")
         print("-------------------------------")

if MENU=='C1':
         print("-------------------------------")
         print("YOUR CHANGE IS",CHANGE)
         print("YOUR ORDER HAS BEEN PROVIDED")
         print("TAKE YOUR BILLS OR RECEIPIT")
         print("THANK YOU AND HAVE A GREAT DAY")
         print("-------------------------------")

if MENU=='C2':
         print("-------------------------------")
         print("YOUR CHANGE IS",CHANGE)
         print("YOUR ORDER HAS BEEN PROVIDED")
         print("TAKE YOUR BILLS OR RECEIPIT")
         print("THANK YOU AND HAVE A GREAT DAY")
         print("-------------------------------")

if MENU=='D1':
         print("-------------------------------")
         print("YOUR CHANGE IS",CHANGE)
         print("YOUR ORDER HAS BEEN PROVIDED")
         print("TAKE YOUR BILLS OR RECEIPIT")
         print("THANK YOU AND HAVE A GREAT DAY")
         print("-------------------------------")

if MENU=='D2':
         print("-------------------------------")
         print("YOUR CHANGE IS",CHANGE)
         print("YOUR ORDER HAS BEEN PROVIDED")
         print("TAKE YOUR BILLS OR RECEIPIT")
         print("THANK YOU AND HAVE A GREAT DAY")
         print("-------------------------------")

if MENU=='E1':
         print("-------------------------------")
         print("YOUR CHANGE IS",CHANGE)
         print("YOUR ORDER HAS BEEN PROVIDED")
         print("TAKE YOUR BILLS OR RECEIPIT")
         print("THANK YOU AND HAVE A GREAT DAY")
         print("-------------------------------")

if MENU=='E2':
         print("-------------------------------")
         print("YOUR CHANGE IS",CHANGE)
         print("YOUR ORDER HAS BEEN PROVIDED")
         print("TAKE YOUR BILLS OR RECEIPIT")
         print("THANK YOU AND HAVE A GREAT DAY")
         print("-------------------------------")

if MENU=='F1':
         print("-------------------------------")
         print("YOUR CHANGE IS",CHANGE)
         print("YOUR ORDER HAS BEEN PROVIDED")
         print("TAKE YOUR BILLS OR RECEIPIT")
         print("THANK YOU AND HAVE A GREAT DAY")
         print("-------------------------------")

if MENU=='F2':
         print("-------------------------------")
         print("YOUR CHANGE IS",CHANGE)
         print("YOUR ORDER HAS BEEN PROVIDED")
         print("TAKE YOUR BILLS OR RECEIPIT")
         print("THANK YOU AND HAVE A GREAT DAY")
         print("-------------------------------")