def prvi_i_zadnji(brojevi):
    if not brojevi:
        return None

    return brojevi[0], brojevi[-1]

lista1 = [10, 20, 30, 40, 50]
rezultat1 = prvi_i_zadnji(lista1)
print(rezultat1)

def min_i_max(brojevi):
    if not brojevi:
        return None

    najmanji = najveci = brojevi[0]

    for num in brojevi[1:]:
        if num < najmanji:
            najmanji = num
        elif num > najveci:
            najveci = num

    return najmanji, najveci

lista2 = [12, 5, 8, 20, -3, 7]
rezultat2 = min_i_max(lista2)
print(rezultat2)