c0 = int(input("Ingrese un número natural: "))
count = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 //= 2
        print(c0)
    else:
        c0 = 3 * c0 + 1
        print(c0)
        
    count += 1

print("pasos = ", count)

