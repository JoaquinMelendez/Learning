number1 = int(input("Ingrese su primer número"))
number2 = int(input("Ingrese su segundo número"))
number3 = int(input("Ingrese su tercer número"))

longest_number = number1

if number2 > longest_number:
    longest_number = number2
    
if number3 > longest_number:
    longest_number = number3
    
print("El número más grande es", longest_number)
