income = float(input("Digite sus ingresos"))

if income < 85528:
    tax = ((income * 0.18) - 556.2)

else:
    tax = 14839.2 + (income-85528) * 0.32

if tax < 0:
    tax = 0


print("Su impuesto a pagar es ", round(tax), " pesos")
