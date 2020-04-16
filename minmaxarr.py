import random

def find_min(array):
    return min(array)


def find_max(array):
    return max(array)


def sortion(array):
    for j in range(1, len(array)):
        for a in range(len(array) - j):
            if array[a] > array[a + 1]:
                array[a], array[a + 1] = array[a + 1], array[a]
    return array


arr = []
leng = int(input('Enter the length of the array: '))
for i in range(leng):
    arr.append(random.randint(0, leng))

print(sortion(arr))
print(find_max(arr))
print(find_min(arr))
