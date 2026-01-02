import pandas as pd

df = pd.read_csv("vendas.csv")

print("--- 1. INSPEÇÃO GERAL ---")
df.info() 
print("\n")

# ---------------------------------------------------------

print("--- 2. FILTRAGEM ---")
# analise da filial a

filtrofiliala = (df['loja'] == 'Filial A') & (df['valor_venda'] > 1000)

vendas_altas = df[filtrofiliala]

print(f"Encontrei {len(vendas_altas)} vendas suspeitas ou de alto valor na Filial A:")
print(vendas_altas)
print("\n")

# ---------------------------------------------------------
# O Desafio: Loja "Filial B" E Vendas > 1000

filtrofilialb = (df['loja'] == 'Filial B') & (df['valor_venda'] > 1000)

vendas_altas = df[filtrofilialb]

print(f"Encontrei {len(vendas_altas)} vendas suspeitas ou de alto valor na Filial B:")
print(vendas_altas)
print("\n")

# ---------------------------------------------------------

# analise da matriz

filtromatriz = (df['loja'] == 'Matriz') & (df['valor_venda'] > 1000)

vendas_altas = df[filtromatriz]

print(f"Encontrei {len(vendas_altas)} vendas suspeitas ou de alto valor na Matriz:")
print(vendas_altas)
print("\n")

# ---------------------------------------------------------

print("--- 3. DETECTANDO OS OUTLIERS ---")

media = df['valor_venda'].mean()
mediana = df['valor_venda'].median()

print(f"Média das vendas: R$ {media:.2f}")
print(f"Mediana das vendas: R$ {mediana:.2f}")

if media > mediana * 2:
    print("ALERTA: A média está muito maior que a mediana.")
    print("Isso confirma: Temos outliers puxando o valor pra cima!")