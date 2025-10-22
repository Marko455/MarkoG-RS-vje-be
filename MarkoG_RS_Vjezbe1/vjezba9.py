def izbaci_duplikate(numbers):
    seen = set()
    unique_numbers = []
    for num in numbers:
        if num not in seen:
            unique_numbers.append(num)
            seen.add(num)
    return unique_numbers

nums = [1, 2, 2, 3, 4, 4, 5, 1]
unique_nums = izbaci_duplikate(nums)
print(unique_nums)
