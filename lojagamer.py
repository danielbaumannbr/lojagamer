import pandas  as pd
import matplotlib as plt
#Carregar o arquivo csv no python
try:
    df=pd.read_csv('vendas game.csv')
except FileNotFoundError:

    print("Arquivo não encontrado.")
    exit()
# Mostra as primeiras linhas do Dataframe
print(df.head())
# Criar uma coluna de total de vendas
df['total_vendas']=df['quantidade']*df['valor']
#agrupar dos dados das vendas dos jogos
vendas_por_jogos=df.groupby('jogo')['total_vendas'].sum().reset_index()
print('\n')
print('Total de vendas por jogo')
print(vendas_por_jogos)
#mostra o jogo mais vendido
jogo_mais_vendido=vendas_por_jogos.sort_values(by='total_vendas',ascending=False).iloc[0]
print(jogo_mais_vendido['jogo'])