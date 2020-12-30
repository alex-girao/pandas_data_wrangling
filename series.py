import pandas as pd

# cria a Series de notas
notas = pd.Series([7.6, 5.0, 8.5, 9.5, 6.4])

# criando as listas de natriculas e nomes
lst_matriculas = ['M02','M05','M13','M14','M19']
lst_nomes = ['Bob','Dayse','Bill','Cris','Jimi']
# criando uma serie onde os indices sao as matriculas e os nomes sao os valores
alunos = pd.Series(lst_nomes,index=lst_matriculas)

# imprimindo as series
print('---- Series Notas ----')
print(notas)
print('---- Series Alunos ----')
print(alunos)

# dicionario
dic_alunos = {'M02':'Bob','M05':'Dayse','M13':'Bill', 'M14':'Cris','M19':'Jimi'}
print('---- Dicionário Alunos ----')
print(dic_alunos)

# serie criada a partir de um dicionario
alunos = pd.Series(dic_alunos)
# atribuindo nomes p/ os vetores
alunos.name = "Alunos"
alunos.index.name = "Matrículas"
print('---- Series Alunos ----')
print(alunos)
print('Número de elementos: ', alunos.size)
print('Vetor de dados: ', alunos.values)
print('Vetor de rótulos: ', alunos.index)
print('Tipo (type): ', type(alunos))
print('dtype das Series: ', alunos.dtype)
print('dtype do vetor de rótulos: ', alunos.index.dtype)