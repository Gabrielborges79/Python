counter = 0

for number in range(6):
    number = float(input())
    if number > 0:
        counter = counter + 1

print(str(counter) + ' valores positivos')