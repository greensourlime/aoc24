f = open('input.txt', 'r')

def compact(churro):
    back_i = len(churro) -1
    for front_i in range(len(churro)):
        if churro[front_i] == '.':
            while back_i > front_i and churro[back_i] == ".":
                back_i -= 1

            if back_i > front_i: 
                churro[front_i], churro[back_i] = churro[back_i], "."

def checksum(churro):
    c_sum = 0
    for i in range(len(churro)):
        if churro[i] == '.':
            break
        c_sum += i * int(churro[i])
    return c_sum

index = 0
block = 0
churro = []
for c in f.read().strip():
    d = int(c)
    if index % 2 == 0:
        churro += ([str(block) for i in range(d)])
        block += 1
    else:
        churro += (["." for i in range(d)])
    index +=1

compact(churro)
print(checksum(churro))