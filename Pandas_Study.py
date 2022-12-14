import pandas as pd

# Acrescentando as 5 planilhas
df1 = pd.read_excel("/content/drive/MyDrive/Datasets/Aracaju.xlsx")
df2 = pd.read_excel("/content/drive/MyDrive/Datasets/Fortaleza.xlsx")
df3 = pd.read_excel("/content/drive/MyDrive/Datasets/Natal.xlsx")
df4 = pd.read_excel("/content/drive/MyDrive/Datasets/Recife.xlsx")
df5 = pd.read_excel("/content/drive/MyDrive/Datasets/Salvador.xlsx")

# Mostrando as 5 primeiras linhas
df1.head()

# Concatenando as 5 planilhas(juntando)
df = pd.concat([df1,df2,df3,df4,df5])

# Mostrando as 5 primeiras linhas após concatenar
df.head()

# Exibindo as 5 ultimas linhas
df.tail()

# Exibindo uma amostra de 5 linhas
df.sample(5)

# Exibe o time de dado de cada coluna
df.dtypes

# Altera o tipe de dado da coluna LojaID
df['LojaID'] = df['LojaID'].astype('object')

# Consulta as linhas sem valores
df.isnull().sum()

# Substituindo os valores nulos pela média
df['Vendas'].fillna(df["Vendas"].mean(), inplace=True)

# Valor medio de vendas
df['Vendas'].mean()

# Substituindo os valores nulos por 0
df['Vendas'].fillna(0, inplace=True)

# Apagando as linhas com valores
df.dropna(inplace=True)

# Apagando as linhas com valores nulos com base em apenas 1 coluna
df.dropna(subset=['Vendas'], inplace=True)

# Apagando linhas que estejam com valores faltando em todas as colunas
df.dropna(how='all',inplace=True)

### CRIANDO NOVAS COLUNAS ###

# Criando a coluna de receita
df['Receita'] = df['Vendas'].mul(df['Qtde'])

df.head()

# Retorna a maior receita
df['Receita'].max()

# Retorna a menor receita
df['Receita'].min()

# nlarest, retorna as 3 linhas com maiores receitas
df.nlargest(3, 'Receita')

# Retorna as 3 piores receitas
df.nsmallest(3, "Receita")

# Agrupando por cidade
df.groupby("Cidade")["Receita"].sum()

# Ordenando o conjunto de  dados
df.sort_values("Receita", ascending=False).head(10)

### TRABALHANDO COM DATAS ###

# Mudando a coluda de data em tipo inteiro
df["Data"] = df["Data"].astype("int64")

# Definindo "Data" como valor de "Data"
df['Data'] = pd.to_datetime(df['Data'], errors='coerce')

# Agrupamento por ano
df.groupby(df["Data"].dt.year)["Receita"].sum()

# Criando uma nova coluna com o Ano
df["Ano_Venda"] = df["Data"].dt.year

# Extraindo o mes e o dia, acrescentando na planilha
df["Mes_venda"], df["Dia_venda"] = (df["Data"].dt.month, df["Data"].dt.day)

# Retornando a data mais antiga
df["Data"].min()

# Calculando a diferença entre dias
df["Diferenca_dias"] = df["Data"] - df["Data"].min()

df.sample(5)

# Criando uma coluna de trimestre
df["Trimestre_venda"] = df["Data"].dt.quarter

# Filtrando as vendas de 2019 do mês de março
vendas_marco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]

# Exibindo a variavel criada acima
vendas_marco_19

### VISUALIZAÇÃO DE DADOS

# Mostra as vendas referente ao LojaID e tras em modo ascendente, do maior pro menor
df["LojaID"].value_counts(ascending=False)

# Grafico com barras
df["LojaID"].value_counts(ascending=False).plot.bar()

# Grafico com barras horizontais
df["LojaID"].value_counts(ascending=True).plot.barh();

# Grafico de pizza
df.groupby(df["Data"].dt.year)["Receita"].sum().plot.pie();

# Total de vendas por cidade
df["Cidade"].value_counts()

# Adicioando o titulo e alterando o nome dos eixos
import matplotlib.pyplot as plt
df["Cidade"].value_counts().plot.bar(title="Total de vendas por Cidade")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas");

# Alterando a cor
df["Cidade"].value_counts().plot.bar(title="Total de vendas por Cidade", color='red')
plt.xlabel("Cidade")
plt.ylabel("Total Vendas");

# Alterando o estilo, tem varios estilos no site do matplotlib
plt.style.use("ggplot")

df.groupby(df["mes_venda"])["Qtde"].sum().plot(title = "Total produtos vendidos x Mes")
plt.xlabel("Mes")
plt.ylabel("Total Produtos vendidos")
plt.legend();

df.groupby(df["mes_venda"])["Qtde"].sum()

# Selecionando apenas as vendas de 2019
df_2019 = df[df["Ano_Venda"] == 2019]

# Total de produtos vendidos por mes
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = ">")
plt.xlabel("Mes")
plt.ylabel("Total de produtos vendidos")
plt.legend();

# Histograma
plt.hist(df["Qtde"], color="dimgrey");

# Grafico de dispersão
plt.scatter(x=df_2019["dia_venda"], y = df_2019["Receita"]);

# Salvando em PNG o grafico
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = ">")
plt.title("Quantidade de produtos vendidos x mês")
plt.xlabel("Mes")
plt.ylabel("Total de produtos vendidos")
plt.legend();
plt.savefig("Grafico QTDE x MES.png")
