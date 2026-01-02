import pandas as pd
import random

# Criando dados fictícios
dados = {
    'data': pd.date_range(start='2024-01-01', periods=100),
    'loja': [random.choice(['Matriz', 'Filial A', 'Filial B']) for _ in range(100)],
    'produto': [random.choice(['Notebook', 'Teclado', 'Mouse', 'Monitor']) for _ in range(100)],
    'valor_venda': [random.randint(50, 500) for _ in range(100)]
}

# DataFrame
df = pd.DataFrame(dados)

# OUTLIERS
df.loc[95, 'valor_venda'] = 15000  # Venda errada ou gigante
df.loc[96, 'valor_venda'] = 50000  # Outro outlier

# Salvar
df.to_csv('vendas.csv', index=False)
print("Arquivo 'vendas.csv' criado com sucesso na pasta Lab-Dados!")