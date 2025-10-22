def filter_parni(numbers):
    return [num for num in numbers if num % 2 == 0]

brojevi = [1, 2, 3, 4, 5, 6, 7, 8]
parni = filter_parni(brojevi)
print(parni)

