largest_number = -9999999999999

while True:
    user_number = input("Escriba un número, si quiere terminar escriba SALIR: ")

    if user_number == '':
        print("No ha introducido ningún número")
        continue
    elif user_number == 'SALIR':
        break

    number = int(user_number)
    
    if number > largest_number:
        largest_number = number


print("El número más grande es: ", largest_number)

