f = open('input.txt', 'r')

def trail_add(next, what):
    if len(next) == 0:
        next = what
    else:
        next += " " + what
    return next

def blink(cl):
    new_class = {}
    for stone_type in cl.keys():        
        if stone_type == '0':
            if '1' in new_class.keys():
                new_class['1'] += cl[stone_type]
            else:
                new_class['1'] = cl[stone_type]
        elif len(stone_type) % 2 == 0:
            cut = int(len(stone_type)/2)
            for part in [str(int(stone_type[:cut])), str(int(stone_type[cut: ]))]:
                if part in new_class.keys():
                    new_class[part] += cl[stone_type]
                else:
                    new_class[part] = cl[stone_type]
        else:
            grow = str(2024 * int(stone_type))
            if grow in new_class.keys():
                new_class[grow] += cl[stone_type]
            else:
                new_class[grow] = cl[stone_type]

    return new_class   
    

stones = f.readline().strip().split()

classify = {}
for stone in stones:
    if stone in classify.keys():
        classify[stone] += 1
    else:
        classify[stone] = 1

for i in range(75):
    classify = blink(classify)

count = 0
for k in classify.keys():
    count += classify[k]

print(count)