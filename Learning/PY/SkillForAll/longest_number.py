number = int(input("Introduce tu número a comparar: "))

longest_number = -99999999999999999999

while number != -1:
    if number > longest_number:
        longest_number = number


        number = int(input("Introduce otro número a comparar: "))

print("El número más grande es ", longest_number)
                     
