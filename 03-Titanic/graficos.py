import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("titanic_raw.csv")
print("Gerando gráfico de sobrevivência por sexo...")

sns.set_style("whitegrid")
plt.figure(figsize=(6, 4))

grafico = sns.barplot(data=df, x="Sex", y="Survived", palette="viridis")

plt.title("Chance de Sobrevivência: Homens vs Mulheres")
plt.ylabel("Chance (0 a 1)")
plt.xlabel("Sexo")

plt.savefig("grafico_sobrevivencia.png")
print("Sucesso! Verifique o arquivo 'grafico_sobrevivencia.png' na sua pasta.")