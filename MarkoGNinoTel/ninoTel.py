import re

def validiraj_broj_telefona() -> dict:
    broj = input("Unesite telefonski broj: ").strip()

    if broj.startswith('+'):
        cisti = '+' + re.sub(r'\D', '', broj[1:])
    else:
        cisti = re.sub(r'\D', '', broj)

    pozivni_mjesta = {
        '01':  'Grad Zagreb i Zagrebačka županija',
        '020': 'Dubrovačko-neretvanska županija',
        '021': 'Splitsko-dalmatinska županija',
        '022': 'Šibensko-kninska županija',
        '023': 'Zadarska županija',
        '031': 'Osječko-baranjska županija',
        '032': 'Vukovarsko-srijemska županija',
        '033': 'Virovitičko-podravska županija',
        '034': 'Požeško-slavonska županija',
        '035': 'Brodsko-posavska županija',
        '040': 'Međimurska županija',
        '042': 'Varaždinska županija',
        '043': 'Bjelovarsko-bilogorska županija',
        '044': 'Sisačko-moslavačka županija',
        '047': 'Karlovačka županija',
        '048': 'Koprivničko-križevačka županija',
        '049': 'Krapinsko-zagorska županija',
        '051': 'Primorsko-goranska županija',
        '052': 'Istarska županija',
        '053': 'Ličko-senjska županija',
        '091': 'Hrvatski Telekom (T-Mobile / bonbon)',
        '092': 'Telemach',
        '095': 'A1 Hrvatska (bivši Vipnet)',
        '097': 'Telemach (bivši Tele2)',
        '098': 'Hrvatski Telekom (T-Mobile)',
        '099': 'A1 Hrvatska (bivši Vipnet)',
        '0800': 'Besplatni pozivi (posebne usluge)',
    }

    lokalni = cisti
    if cisti.startswith('+385'):
        lokalni = '0' + cisti[4:]

    pozivni = None
    mjesto = None

    for p in sorted(pozivni_mjesta.keys(), key=len, reverse=True):
        if lokalni.startswith(p):
            pozivni = p
            mjesto = pozivni_mjesta[p]
            break

    rezultat = {
        "broj": cisti,
        "pozivni": pozivni,
        "mjesto": mjesto,
        "validan": pozivni is not None
    }

    return rezultat

if __name__ == "__main__":
    rezultat = validiraj_broj_telefona()
    print("\nRezultat validacije:")
    print(rezultat)
