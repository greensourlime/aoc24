f = open('input.txt', 'r')

def trail_add(next, what):
    if len(next) == 0:
        next = what
    else:
        next += " " + what
    return next

stones = f.readline().strip().split()
final = ""
for stone in stones:
    trail = stone
    for i in range(25):     
        trail = trail.split(" ")
        next = ""
        for bit in trail:
            if bit == '0':
                next = trail_add(next, '1')
            elif len(bit) % 2 == 0:
                cut = int(len(bit)/2)
                next = trail_add(next, str(int(bit[:cut])) + " " + str(int(bit[cut: ])))
            else:
                next = trail_add(next, str(2024 * int(bit)))
        trail = next
    final += " " + trail

final = final[1:]

print(len(final.split(" ")))