import pandas as pd

with open('9_ABC.csv', encoding='utf-8') as file:
    data_1 = pd.read_csv(file, sep=';')

with open('3_ABC.csv', encoding='utf-8') as file:
    data_2 = pd.read_csv(file, sep=';')

with open('4_ABC.csv', encoding='utf-8') as file:
    data_3 = pd.read_csv(file, sep=';')

with open('8_ABC.csv', encoding='utf-8') as file:
    data_4 = pd.read_csv(file, sep=';')

data = pd.concat([data_1, data_2, data_4, data_3])
data = data[['Емкость', 'Оператор']]
Op = data.groupby('Оператор').sum().sort_values(by='Емкость', ascending=False)
Op = Op.iloc[0:10]
print(Op)
