f = open('input.txt', 'r')

def get_blocks(churro):
    blocks = []
    i = len(churro)-1

    while i>=0:
        while i>=0 and churro[i] == '.':
            i -= 1
        if i>=0:
            last_elem = i
            elem = churro[i]
            while i>=0 and churro[i] == elem:
                i -= 1
            first_elem = i + 1
            blocks.append((elem, 1+last_elem-first_elem, first_elem, last_elem))
    return blocks

def fit_block(churro, blocks):    
    i = 0
    n = len(churro)
    while i < block[2]:
        while i < block[2] and churro[i] != '.':
            i += 1
        if  i < block[2]:
            hole_size = i
            while  i <= block[2] and churro[i] == '.':
                i += 1
            hole_size = i - hole_size

            if block[1] <= hole_size and block[2] >= i:
                move_it(churro, block, i - hole_size)                
                return
            
def move_it(churro, block, new_index):
    for i in range(block[1]):
        churro[new_index + i] = block[0]
        churro[block[2] + i] = '.'

def checksum(churro):
    c_sum = 0
    for i in range(len(churro)):
        if churro[i] != '.':
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

blocks = get_blocks(churro)
for block in blocks:
    fit_block(churro, block)

print(checksum(churro))