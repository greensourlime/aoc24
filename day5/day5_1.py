f = open('input.txt', 'r')

def check_rules(page_list):
    for a, b in rules:
        if a in page_list and b in page_list:
            if page_list.index(a) > page_list.index(b):
                return False
    return True

blocks = f.read().split("\n\n")
rules_block = blocks[0].splitlines()
sequences_block = blocks[1].splitlines()

rules = []
for r in rules_block:
    a, b = map(int, r.split("|"))
    rules.append((a,b))

sum_of_mids = 0
for seq in sequences_block:
    pages = list(map(int, seq.split(",")))
    if check_rules(pages):
        sum_of_mids += pages[len(pages) // 2]

print(sum_of_mids)

