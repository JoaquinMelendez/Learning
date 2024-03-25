longest_number = -99999999999999999999

while True:
    number = int(input("Introduce tu número a comparar (-1 para salir): "))
    if number == -1:
        break
    if number > longest_number:
        longest_number = number

print("El número más grande es", longest_number)
