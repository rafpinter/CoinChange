"""

Tool to find the minium number of coins that you must have to give change.

"""

# Prompts for the money
while True:
    money = float(input("Cash owed: ")) * 100
    if money > 0:
        break

soma = 0

# Iterate until 
for j in [25, 10, 5, 1]:
    subtotal = 0
    while money >= j:
        money = money - j
        soma = soma + 1
        subtotal +=1
    if subtotal != 0:
        print(f"{j}¢:", subtotal)

print("Minimum coin number:", soma)