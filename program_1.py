#программа нахождения суммы между минимальным и максимальным значением в массиве
numbers = [0,1,2,3,4]
size = 5
index = 0
max = numbers[index]
min = numbers[index]
index_max = 0
index_min = 0
sum = 0
stop = 0
while index < size :
    if numbers[index] >= max :
        max = numbers[index]
        index_max = index
    if numbers[index] <= min :
        min = numbers[index]
        index_min = index
    index = index + 1
if index_max > index_min :
    index = index_min
    stop = index_max
elif index_max < index_min :
    index = index_max
    stop = index_min
while index < stop-1 :
    index = index + 1
    sum = sum + numbers[index]
print(sum)