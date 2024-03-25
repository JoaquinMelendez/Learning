height = int(input("¿De cuántos guiones de alto quieres el triángulo?\n"))

print("Triángulo:")
for i in range(1, height + 1):
    print("|" + " " * (height - i) + "/" * i + "\\" * i + " " * (height - i) + "|")

print("+" + (2 * height) * "-" + "+")

