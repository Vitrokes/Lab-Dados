import pandas as pd
df = pd.read_csv("titanic_raw.csv")
print("--- 1. INSPEÇÃO GERAL DOS DADOS ---")
df.info()
print("\n")
print("Aqui estão as primeiras 5 linhas do dataset para você conhecer os passageiros:")
print(df.head())
print("\n")
# ---------------------------------------------------------
print("--- 2. ANÁLISE EXPLORATÓRIA ---")
print("Número total de passageiros:", len(df))
print("Tabela, linhas e colunas:")
print(df.shape)
print("\n")
# ---------------------------------------------------------
print("Colunas mais importantes:")
print(df.columns.tolist())
print("\n")
print("Para saber quem vamos dar prioridade no salvamento, vamos analisar algumas colunas: ID, sexo e idade, priorizando mulheres e crianças")
print("\n")
print("Criando uma tabela com as colunas de interesse:")
colunas_interesse = ['PassengerId', 'Sex', 'Age']
tabela_interesse = df[colunas_interesse]
print(tabela_interesse)
print("\n")

print("Agora, filtrando apenas mulheres e crianças (idade < 18):")
filtro = (tabela_interesse["Age"] < 18) | (tabela_interesse["Sex"] == 'female')
passageiros_prioritarios = tabela_interesse[filtro]
print(passageiros_prioritarios)
print("Número total de passageiros prioritários (mulheres e crianças):", len(passageiros_prioritarios))
print("\n")
print(f"Pessoas com idade desconhecida: {df['Age'].isnull().sum()}")
print("\n")
# ---------------------------------------------------------
print("--- 3. ANÁLISE DE MÉDIAS ---")
idade_media = df['Age'].mean()
print(f"A idade média dos passageiros é: {idade_media:.2f} anos")
print("\n")
print("Analisando o preço médio das passagens:")
preco_medio = df['Fare'].mean()
print(f"O preço médio das passagens é: ${preco_medio:.2f}")
print("\n")
# ---------------------------------------------------------"

print("--- 4. DETECTANDO MAIS NOVO E MAIS VELHO A BORDO ---")
# 1. Definir quais colunas queremos ver no final (pra não virar bagunça)
colunas = ['PassengerId', 'Name', 'Sex', 'Age','Survived']

print("--- O MAIS NOVO E O MAIS VELHO ---")

# 2. Descobrir os números extremos
menor_idade = df['Age'].min()
maior_idade = df['Age'].max()

print(f"A menor idade registrada é: {menor_idade} anos")
print(f"A maior idade registrada é: {maior_idade} anos")
print("\n")

# 3. Filtrar os passageiros que correspondem a esses extremos
bebe_a_bordo = df[df['Age'] == menor_idade]
anciao_a_bordo = df[df['Age'] == maior_idade]

print("--- Detalhes do passageiro mais Jovem ---")
print(bebe_a_bordo[colunas])
print("\n")

print("--- Detalhes do passageiro mais Velho ---")
print(anciao_a_bordo[colunas])

# ---------------------------------------------------------
print("--- 5. A VERDADE SOBRE A SOBREVIVÊNCIA ---")

# A Porcentagem Geral por Sexo
taxa_sobrevivencia = df.groupby('Sex')['Survived'].mean()

print("Chance de sobreviver (em %):")
print(taxa_sobrevivencia * 100)