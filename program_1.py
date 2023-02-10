#программа нахождения максимального и минимального индекса в массиве
numbers = [9,9,3,5,9]
size = 5
index = 0
max = numbers[index]
min = numbers[index]
index_max = 0
index_min = 0
while index < size :
    if numbers[index] >= max :
        max = numbers[index]
        index_max = index
    if numbers[index] <= min :
        min = numbers[index]
        index_min = index
    index = index + 1
print(index_max)