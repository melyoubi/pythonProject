#lista
mesos = ['Gener', 'Febrer', 'Març', 'Abril', 'Maig', 'Juny', 'Juliol', 'Agost', 'Septembre', 'Octubre', 'Novembre', 'Desembre']
dia = int(input())
mes = int(input())
any = int(input())
data = str(dia) + ' de ' + mesos[mes-1] + ' del ' + str(any)
print(data)