import random

numero_secreto = random.randrange(1, 4)

print(
"""
+================================+
| ¡Q PASA WN, QUEASTE ATRAPAO EN |
| MI JUEGO! WAJAJAJA             |
| TENI QUE ACHUNTARLE A UN NUMERO|
| DEL 1 AL 100 PA SALIR DE MI    |
| BUCLE INFINITO WAJA XD         |
+================================+
""")

number = int(input("Escribe tu numerito aki: "))

while number != numero_secreto:
    print("WA COXINO QLO NO LE AXUNTASTE XD")
    number = int(input("Escribe tu número acá: "))
    
print("PERO WN, COMO LO HICISTE COXINO QLOOOO QWEA, VALE XORETE TE SALIO WENA") 
