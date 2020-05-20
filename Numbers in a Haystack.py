import re

y = []
with open('regex_sum_440546.txt') as fh:
    for line in fh:
        x = re.findall('[0-9]+', line)
        for i in x:
            y.append(int(i))
    print(y)
    z = sum(y)
    print(z)
