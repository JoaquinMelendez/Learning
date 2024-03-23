
print("Qué quieres ejecutar? Escriba un número\n 1-km a ml\n 2-ml a km")
answer = int(input())

if answer == 1:
    km = float(input("Escriba su cantidad de km:"))
    km_to_ml = km*1.61
    print(km, "son", km_to_ml, "millas")
else:
    ml = float(input("Escriba su cantidad de ml"))
    ml_to_km = ml/1.61
    print(ml, "millas son", ml_to_km, "kilometros")



