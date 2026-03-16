#Vending Machine

#introduction to my vending machine
print('''___𝑾𝑬𝑳𝑪𝑶𝑴𝑬 𝑻𝑶 𝑻𝑯𝑬 𝑴𝑶𝑯𝑫 𝑨𝑫𝑰𝑳 𝑯𝑶𝑺𝑺𝑨𝑰𝑵 𝑽𝑬𝑵𝑫𝑰𝑵𝑮 𝑴𝑨𝑪𝑯𝑰𝑵𝑬___''')

print("___𝑾𝑬𝑳𝑪𝑶𝑴𝑬 𝑻𝑶 𝑻𝑯𝑬 𝑴𝑬𝑵𝑼!!___")

print("___𝑯𝑶𝑾 𝑪𝑨𝑵 𝑰 𝑯𝑬𝑳𝑷 𝒀𝑶𝑼___")



#items of vending machine
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

MENU = {
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

#enter the code for which items you want.
selection=input("ENTER THE CODE OF THE ITEMS FOR PURCHASE: ")

if selection == "A1":
    print("You selected A1.")
elif selection == "A2":
    print("You selected A2.")
elif selection == "B1":
    print("You selected B1.")
elif selection == "B2":
    print("You selected B2.")
elif selection == "C1":
    print("You selected C1.")
elif selection == "C2":
    print("You selected C2.")
elif selection == "D1":
    print("You selected D1.")
elif selection == "D2":
    print("You selected D2.")
elif selection == "E1":
    print("You selected E1.")
elif selection == "E2":
    print("You selected E2.")
elif selection == "F1":
    print("You selected F1.")
elif selection == "F2":
    print("You selected F2.")

#select the item from the menu.
if selection in MENU:

    ITEM = MENU[selection]

    PRICE = ITEM['price']

#insert the money
MONEY= float(input("ENTER THE MONEY YOU WANT TO INSERT: "))

#money to the customers
CHANGE= MONEY-PRICE

print(f"Dispensing {ITEM['NAME']}")

print(f"CHANGE: {CHANGE:.2f}")

print("thank you and have a nice day")