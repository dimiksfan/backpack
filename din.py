import csv


def get_lst(file_name, sep=','):
    with open(file_name) as f:
        reader = csv.reader(f, delimiter=sep)
        return [line for line in reader][1:]
    

lst = get_lst('numbers.csv')
items = []
maxW = 100
for elm in lst:
    items.append(list(map(int,elm[0].split(';')))[1:])
items = sorted(items)
print(items)
count = len(items)
max_w = 100
step = 10
tab = []
count_rows = max_w//step
print()
for row in range(0, max_w+1, step):
    tab.append([[0.0] for col in range(count)])


for row in range(count_rows+1):
    for col in range(count):
        if row*step >= items[col][0]:
            tab[row][0] = items[col][:]


for col in range(1, count):
    for row in range(count_rows+1):
        pos_w = row * step - items[col][0]
        row_w = pos_w // step
        if row >= 0:
            if tab[row][col-1][1] <= tab[row_w][col-1][1] + items[col][1]:
                tab[row][col][0] <= tab[row_w][col-1][0] + items[col][0]
                tab[row][col][1] <= tab[row_w][col-1][1] + items[col][1]
            else:
                tab[row][col] = tab[row][col-1]


for row in tab:
    print(row[-1])
