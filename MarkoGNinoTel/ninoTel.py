import re

def validiraj_broj_telefona(broj: str) -> str | None:
    broj = broj.strip()

    if broj.startswith('+'):
        cisti = '+' + re.sub(r'\D', '', broj[1:])
    else:
        cisti = re.sub(r'\D', '', broj)

    dopusteni_pozivni = [
        '01', '020', '021', '022', '023', '031', '032', '033', '034', '035',
        '040', '042', '043', '044', '047', '048', '049','051', '052', '053', 
        '091', '092', '095', '097', '098', '099', '0800'
    ]

    dopustena_mjesta = [
        'Grad Zagreb i Zagrebacka zupanija', "Dubrovacko-neretvanska zupanija", "Splitsko-dalmatinska zupanija", "Sibensko-kninska zupanija", "Zadarska zupanija",
        "Osjecko-baranjska zupanija", "Vukovarsko-srijemska zupanija", "Viroviticko-podravska zupanija", "Pozesko-slavonska zupanija", "Brodsko-posavska zupanija",
        "Medimurska zupanija", "Varazdinska zupanija", "Bjelovarsko-bilogorska zupanija", "Sisacko-moslavacka zupanija", "Karlovacka zupanija", "Koprivnicko-krizevacka zupanija",
        "Krapinsko-zagorska zupanija", "Primorsko-goranska zupanija", "Istarska zupanija", "Licko-senjska zupanija", "A1 Hrvatska", "Tomato", "Telemach", "bonbon",
        "Hrvatsko Telekom", "Besplatni pozivi", "Komercijalni pozivi", "Glasovanje telefonom", "Usluge s neprimjerenim sadrzajem", "Nagradne igre", "Usluge namjenjene djeci",
        "jedinstveni pristupno broj za cijelu drzavu za posebne usluge"
    ]

    lokalni = cisti
    if cisti.startswith('+385'):
        lokalni = '0' + cisti[4:]

    if any(lokalni.startswith(p) for p in dopusteni_pozivni):
        return cisti
    else:
        return None
