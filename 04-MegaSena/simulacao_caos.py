import pandas as pd
import random
import time

print("--- SISTEMA CAIXA - SIMULAÇÃO MEGA DA VIRADA 2025 ---")
print("Status: Iniciando recebimento de pacotes de dados...")
print("\n")

# Funcao para gerar apostas falsas rapido
def gerar_lote_apostas(origem, qtd):
    print(f"--> Recebendo {qtd} apostas do servidor: {origem}...")
    
    # Simulando dados: ID da aposta, Data, e os 6 numeros
    dados = {
        'id_aposta': [f"{origem}-{i}" for i in range(1, qtd + 1)],
        'origem': [origem] * qtd,
        'timestamp': [pd.Timestamp.now()] * qtd,
        # Vamos gerar apenas uma string de numeros pra ser mais leve pro seu PC
        'numeros': [f"{random.randint(1,60)}-{random.randint(1,60)}-..." for _ in range(qtd)]
    }
    
    # Simulando delay de rede (o servidor "pensando")
    time.sleep(1.5) 
    return pd.DataFrame(dados)

# 1. O FLUXO INTENSO (Simulando volume alto)
# Vamos fazer números menores pra não travar seu PC, mas imagine milhões aqui
volume_app = 50000      
volume_lotericas = 60000 

# Criando os DataFrames separados (Silos de Dados)
df_app = gerar_lote_apostas("APP_MOBILE", volume_app)
df_fisico = gerar_lote_apostas("LOTERICA_FISICA", volume_lotericas)

print("\n")
print("--- ALERTA: FIM DO PRAZO DE APOSTAS (17:00) ---")
print("Iniciando a Consolidação (Merge) dos dados para o Sorteio...")
print("Isso pode demorar devido à sobrecarga...")

# 2. O MOMENTO DO TRAVAMENTO (Atraso)
inicio_processamento = time.time()

# Concatenando (Juntando) as duas tabelas gigantes
# O comando pd.concat é como colar uma planilha embaixo da outra
df_total = pd.concat([df_app, df_fisico])

# Simulando um processamento pesado (ordenar 110.000 linhas por data)
df_total = df_total.sort_values(by='timestamp')

fim_processamento = time.time()
tempo_gasto = fim_processamento - inicio_processamento

print(f"\nDados consolidados em {tempo_gasto:.4f} segundos.")
print(f"Total de apostas processadas: {len(df_total)}")

# 3. A AUDITORIA (O motivo real do atraso?)
# Imagine que precisam verificar se não tem ID duplicado (fraude)
print("\n--- INICIANDO AUDITORIA DE INTEGRIDADE ---")

# Vamos simular que o sistema encontrou um erro (ID duplicado vindo de lugares diferentes)
# Criando um erro artificial pra testar:
df_total.loc[100, 'id_aposta'] = 999999 # Criando uma aposta bugada

duplicadas = df_total[df_total.duplicated(subset=['id_aposta'], keep=False)]

if len(duplicadas) > 0:
    print("❌ ERRO CRÍTICO: Detectamos colisão de IDs!")
    print("O sorteio NÃO pode ocorrer até resolvermos isso.")
    print(f"Apostas com problemas encontradas: {len(duplicadas)}")
    print(duplicadas.head())
else:
    print("✅ Auditoria OK. O sistema está liberado para o sorteio!")