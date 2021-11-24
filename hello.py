#lista
mesos = ['Gener', 'Febrer', 'Març', 'Abril', 'Maig', 'Juny', 'Juliol', 'Agost', 'Septembre', 'Octubre', 'Novembre', 'Desembre']
dia = 23
mes = int(input())
any = 2020
data = str(dia) + ' de ' + mesos[mes-1] + ' del ' + str(any)
print(data)
