x = int(input("De cuantos guiones de alto quieres el rectangulo?\n"))
y = int(input("¿De cuantos guinoes de ancho quieres el rectangulo?\n"))

print("+" + y * "-" + "+")
print(("|" + " " * y + "|\n") * x, end = "")
print("+" + y * "-" + "+")
