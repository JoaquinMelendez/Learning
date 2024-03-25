print("¿Qué quieres hacer? Escoge un número \n1- kg a lb \n2-lb a kg")
resp = float(input())

if resp == 1:
    print("Escribe la cantidad de kilos")
    cant = float(input())
    trad = cant*2.20462

    print(cant, "kilos son", round(trad, 2), "libras")
else:
    print("Escribe la cantidad de libras")
    cant = float(input())
    trad = cant/2.20462

    print(cant, "libras son", round(trad, 2), "kilos")
