flower_dict = {
0: 'Полевые цветы',
1: 'Липа',
2: 'Клен',
3: 'Гречка',
4: 'Вереск',
5: 'Яблоня',
6: 'Малина',
7: 'Одуванчик',
8: 'Вишня',
9: 'Черемуха'}


def sorting(arrry):
    for i in range(1, len(arrry) + 1):
        for j in range(len(arrry) - i):
            if arrry[j] > arrry[j+1]:
                arrry[j], arrry[j+1] = arrry[j+1], arrry[j]
    return arrry


indexes = []
honey_mass = [0 for i in range(10)]


for i in range(11):
    honey_type = int(input('Enter code of honey type: '))
    if honey_type < 0:
        break
    mass = int(input('Enter mass of chosen honey type: '))
    honey_mass[honey_type] = mass
    print()
mass_dict = {}
for i in honey_mass:
    mass_dict[i] = honey_mass.index(i)
sorted_arr = sorting(honey_mass)

for i in range(10):
    indexes.append(mass_dict[sorted_arr[i]])
for i in range(10):
    print(flower_dict[indexes[i]])


