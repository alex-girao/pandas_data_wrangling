import pandas as pd

# cria a Series de notas
notas = pd.Series([7.6, 5.0, 8.5, 9.5, 6.4])

# cria a Series alunos
lst_matriculas = ['M02','M05','M13','M14','M19']
lst_nomes = ['Bob','Dayse','Bill','Cris','Jimi']
# especificando as matriculas como indices
alunos = pd.Series(lst_nomes,index=lst_matriculas)

# imprimindo as series
print("---- NOTAS ----");
print(notas); 
print("---- ALUNOS ----");
print(alunos);