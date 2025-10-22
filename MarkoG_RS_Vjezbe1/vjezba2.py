godina = int(input("Unesite godinu:"))

if godina % 4 and godina % 100 != 0 or godina % 400:
    print("Godina je prijestupna.")
else:
    print("Godina nije prijestupna.")