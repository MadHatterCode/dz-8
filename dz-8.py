example_list = [1, 3, 5]
# example_list = [6]
# example_list = []

summa = 0
for i, num in enumerate(example_list):
    if i % 2 == 0:
        summa += num
    if i == len(example_list) - 1:
        summa = summa * num
print(summa)
