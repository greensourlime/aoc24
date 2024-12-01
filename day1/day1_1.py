f = open('input.txt', 'r')

first_list = []
second_list = []
for l in f.readlines():
    first, second = map(int, l.split())
    first_list.append(first)
    second_list.append(second)

first_list.sort()
second_list.sort()

distances_sum = sum( abs(a - b) for a, b in zip(first_list, second_list) )

print(distances_sum)
