import random

nasumican_broj = random.randint(1, 100)

while True:
    guess = input("Unesi broj: ")
    guess = int(guess)

    if guess < nasumican_broj:
        print("Uneseni broj je preniski. Pokusaj opet.")
    elif guess > nasumican_broj:
        print("Uneseni broj je previsok. Pokusaj opet.")
    else:
        print(f"Bravo, nasumican broj je: {nasumican_broj}.")
        break