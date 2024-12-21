from datetime import datetime

from dateutil.relativedelta import relativedelta

valor_total = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos

data_parcelas = []
data_parcela = data_emprestimo
while data_parcela < data_final:
    data_parcelas.append(data_parcelas)
    data_parcela += relativedelta(month=+ 1)

numero_parcelas = len(data_parcelas)

for data in data_parcelas:
    print(data)

print(numero_parcelas)