# Estudo Dataframe
import pandas as pd

# Lista: Uma coleção ordenada de elementos que podem ser de qualquer tipo
lista_nomes = ['Ana', 'Marcos', 'Carlos']
print('Lista de nome: \n', lista_nomes[0])

# Dicionário: Estrutura composta de pares chave-valor

dicionario_pessoa = {
    'nome':'Ana',
    'idade':20,
    'cidade': 'São Paulo'
}
print('Dicionário de uma pessoa: \n', dicionario_pessoa)
print('Atributo do Dicionário: \n', dicionario_pessoa.get('nome'))

# Lista de dicionários: Estrutura de dados que combina listas e dicionários
dados = [
    {'nome':'Ana', 'idade':20,'cidade':'São Paulo'},
    {'nome':'Marcos', 'idade':25,'cidade':'São José dos Campos'},
    {'nome':'Carlos', 'idade':35,'cidade':'Rio de Janeiro'},
]

# DataFrame: Estrutura de dados bidimensional
df = pd.DataFrame(dados)
print('DataFrame \n', df)

# Selecionar coluna
print(df['nome'])

# Selecionar várias colunas
print(df[['nome','idade']])

# Selecionar linhas pelo índice
print('Primeira linha \n', df.iloc[2])

# Adicionar uma nova coluna
df['salario'] = [4100, 3600, 5200]

# Adicionar um novo registro
df.loc[len(df)] = {
    'nome':'João',
    'idade':30,
    'cidade':'Taubaté',
    'salario':4800
}
print('DataFrame Atual \n', df)

# Removendo uma coluna
df.drop('salario', axis=1,inplace=True)

# Filtrando pessoas com mais de 29 anos
filtro_idade = df[df['idade'] >=30]
print('Filtro \n', filtro_idade)

# Salvando o DataFrame em um arquivo CSV
df.to_csv('dados.csv', index=False)

#Lendo um Arquivo CSV em um DataFrame
df_lido = pd.read_csv('dados.csv')
print('\n Leitura do CSV \n', df_lido)