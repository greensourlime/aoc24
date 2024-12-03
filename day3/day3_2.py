import re
f = open('input.txt', 'r')

def sum_muls(scrap):
    patron = r"(do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\))"
    all_commands = re.findall(patron, scrap)
    it_counts = True
    partial_sum = 0
    for com in all_commands:
        if com[0] == "do()":
            it_counts = True
        elif com[0] == "don't()":
            it_counts = False         
        elif "mul" in com[0] and it_counts:
                partial_sum += int(com[1]) * int(com[2])

    return partial_sum

print(sum_muls("".join(f.readlines())))