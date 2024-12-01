f = open('input.txt', 'r')

first_list = []
second_list = []
for l in f.readlines():
    first, second = map(int, l.split())
    first_list.append(first)
    second_list.append(second)

#times_sum = 0
#for n in first_list:
    #times_sum += n * second_list.count(n)
times_sum = sum(n * second_list.count(n) for n in first_list)

print(times_sum)
