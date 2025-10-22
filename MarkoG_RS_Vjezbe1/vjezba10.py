def brojanje_rijeci(text):
    rijeci = text.lower().split()
    
    rijeci = [rijec.strip('.,!?;:"\'()[]{}') for rijec in rijeci]
    
    word_count = {}
    for rijec in rijeci:
        if rijec:
            word_count[rijec] = word_count.get(rijec, 0) + 1

    return word_count

text = "Python je programski jezik koji je jednostavan za ucenje i koristenje, Python je vrlo popularan."
counts = brojanje_rijeci(text)
print(counts)