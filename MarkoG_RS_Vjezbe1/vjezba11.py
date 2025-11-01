def razdvoji_brojeve(numbers):
    parni_brojevi = []
    neparni_brojevi = []
    
    for num in numbers:
        if num % 2 == 0:
            parni_brojevi.append(num)
        else:
            neparni_brojevi.append(num)
    
    return parni_brojevi, neparni_brojevi

brojevi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parni, neparni = razdvoji_brojeve(brojevi)
print("Parni brojevi:", parni)
print("Neparni brojevi:", neparni)