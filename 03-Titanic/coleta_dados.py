import pandas as pd

print("A iniciar o download dos dados do Titanic...")

# URL direta do dataset (fonte confiável: DataScienceDojo)
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

# O Pandas é tão incrível que lê direto da internet!
df = pd.read_csv(url)

# Salvando no seu computador para não precisar baixar toda vez
df.to_csv("titanic_raw.csv", index=False)

print("Sucesso! O arquivo 'titanic_raw.csv' foi salvo na pasta.")
print("-" * 30)
print("Primeiras 5 linhas para você conhecer os passageiros:")
print(df.head())