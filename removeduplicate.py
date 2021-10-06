numbers = [1, 1, 2, 4, 4, 7, 8]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)