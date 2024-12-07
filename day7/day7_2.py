f = open('input.txt', 'r')

def backtrack_test(target, numbers, index, acum):
    if acum is None:
        acum = numbers[0]
        index = 1

    if index == len(numbers):
        return acum == target
    
    next_num = numbers[index]

    if backtrack_test(target, numbers, index + 1, acum + next_num):
        return True
    if backtrack_test(target, numbers, index + 1, acum * next_num):
        return True
    if backtrack_test(target, numbers, index + 1, int(str(acum) + str(next_num))):
        return True
    
    return False


res_sum = 0
for l in f.readlines():
    r, ns = l.split(": ")
    res = int(r)
    nums = list(map(int, ns.split(" ")))
    if backtrack_test(res, nums, 0, None):
        res_sum += res

print(res_sum)