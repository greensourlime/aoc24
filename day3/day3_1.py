import re
f = open('input.txt', 'r')

def sum_muls(scrap):
    patron = r"mul\((\d{1,3}),(\d{1,3})\)"
    all_muls = re.findall(patron, scrap)
    return sum(int(a) * int(b) for a, b in all_muls)

total_sum = 0
for l in f.readlines():
    total_sum += sum_muls(l)

print(total_sum)
