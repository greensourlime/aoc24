f = open('input.txt', 'r')

def sorted_seq(page_list):
    result = []
    for num in page_list: # elemento a elemento de la lista desordenada
        already_in = False # por si la lista esta vacia o no hay reglas al respecto o no hay numeros insertados que nos sujeten a nada
        for i, elem in enumerate(result): # asi pillamos los indices, to fancy, para cada elemento ya insertado... 
            if (num, elem) in rules: # hay una regla que dice que va antes de ese
                result.insert(i, num)  # luego lo insertamos justo ahi
                already_in = True
                break # y nos vamos a por otro numero
        if not already_in:
            result.append(num)
    
    return result

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
    if not check_rules(pages):        
        sum_of_mids += sorted_seq(pages)[len(pages) // 2]

print(sum_of_mids)

