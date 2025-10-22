a = float(input("Unesi prvi broj:"))
b = float(input("Unesi drugi broj:"))
operacija = input("Unesi operaciju:")

if operacija == "+":
    rezultat = a + b
elif operacija == "-":
    rezultat = a - b
elif operacija == "*":
    rezultat = a * b
elif operacija == "/":
    if b != 0:
        rezultat = a/b
    else:
        print("Dijeljenje sa nulom nije dozvoljeno.")
else:
    print("Nepodrzani operator")

print("Rezultat operacije ", a, operacija, b, "je: ", rezultat)