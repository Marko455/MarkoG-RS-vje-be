def count_vowels_consonants(text: str) -> dict:
    vowels = set("aeiouAEIOU")
    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return {"vowels": vowel_count, "consonants": consonant_count}


rezultat = count_vowels_consonants("Python je programski jezik koji je jednostavan za ucenje i koristenje, Python je vrlo popularan.")
print(rezultat)