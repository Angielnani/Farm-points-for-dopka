import pandas as pd

with open('9_ABC.csv', encoding='utf-8') as file:
    df = pd.read_csv(file, sep=';')
df = df[['От', 'До', 'Оператор', 'Регион']]
result = []


def find_number(ot, do):
    numbers = []
    for i in range(int(ot), int(do) + 1):
        if len(str(i)) != 7:
            continue
        if len(set(str(i))) == 2:
            numbers.append(i)
        return numbers


for _, ot, do, op, reg in df.itertuples(name=None):
    if len(str(ot)) != 7:
        continue
    for number in find_number(ot, do):
        result.append((number, op, reg))
print(result)
