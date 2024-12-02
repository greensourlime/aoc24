f = open('input.txt', 'r')

def check(report):
    if not all(report[i] <= report[i+1] for i in range(len(report) - 1)): # checking ascending
        if not all(report[i] >= report[i+1] for i in range(len(report) - 1)): # checking descending
            return False

    return all(1 <= abs(report[i] - report[i+1]) <= 3 for i in range(len(report) - 1))

safe_reports = 0
for l in f.readlines():
    report = list(map(int, l.split()))
    
    if check(report):
        safe_reports += 1

print(safe_reports)
