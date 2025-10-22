n = int(input("Unesi broj: "))

faktorijel_for = 1
for i in range(1, n + 1):
    faktorijel_for *= i

print(f"Faktorijel od {n} koristeci for petlju je: {faktorijel_for}")

faktorijel_while = 1
i = 1
while i <= n:
    faktorijel_while *= i
    i += 1

print(f"Faktorijel od {n} koristeci while petlju je: {faktorijel_while}")
