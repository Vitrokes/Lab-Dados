import pandas as pd
import time
import queue
import random

print("--- SIMULAÇÃO: O GARGALO DA VÉSPERA (19h - 20h) ---")

# 1. CONFIGURAÇÃO DO SERVIDOR
capacidade_banco_dados = 100  # O DB só consegue salvar 100 apostas por "rodada"
tamanho_da_fila_servidor = 500 # A memória do servidor só segura 500 pedidos na espera
volume_de_apostadores = 2000   # Muita gente tentando ao mesmo tempo!

# Filas e Listas
fila_processamento = queue.Queue(maxsize=tamanho_da_fila_servidor)
tabela_financeira = [] # Dinheiro que entrou
tabela_apostas = []    # Bilhetes que realmente foram salvos
lista_estorno = []     # Quem se deu mal e vai receber o dinheiro de volta

print(f"👥 Usuários tentando apostar: {volume_de_apostadores}")
print(f"💾 Capacidade do Banco de Dados: {capacidade_banco_dados} apostas/segundo")
print(f"📦 Tamanho máximo da fila interna: {tamanho_da_fila_servidor}")
print("-" * 50)

# 2. Simulando o loop de requisições
print("Iniciando processamento das requisições...")

for usuario_id in range(1, volume_de_apostadores + 1):
    
    # PASSO A: O Pagamento
    # O banco quase nunca cai, então o dinheiro sai da conta.
    tabela_financeira.append({"id": usuario_id, "valor": 5.00, "status": "PAGO"})
    
    # PASSO B: Tentar entrar na fila do Banco de Dados da Caixa
    try:
        # Tenta colocar na fila. Se estiver cheia, dá erro imediato (nowait)
        fila_processamento.put(usuario_id, block=False)
    except queue.Full:
        # AQUI É O PROBLEMA QUE VOCÊ VIU!
        # O sistema pegou o dinheiro, mas não cabe mais nada na fila de gravação.
        # O usuário recebe um "Erro" na tela ou timeout, mas o Pix já foi.
        pass 

# 3. O SERVIDOR TENTANDO SALVAR (Lado do Banco de Dados)
# Vamos tentar esvaziar a fila e salvar no disco
print("\n--- PROCESSANDO A FILA (O DB TENTANDO SALVAR) ---")

apostas_processadas = 0
while not fila_processamento.empty():
    
    # Simulando limite físico: O DB só aguenta salvar X por vez
    if apostas_processadas >= capacidade_banco_dados:
        print("🔥 O BANCO DE DADOS SOBREAQUECEU! PARANDO GRAVAÇÃO AGORA.")
        break # O sistema cai ou o tempo acaba (20h00)
    
    id_sortudo = fila_processamento.get()
    tabela_apostas.append({"id": id_sortudo, "bilhete": f"MEG-{random.randint(1000,9999)}"})
    apostas_processadas += 1

print(f"Total de apostas salvas com sucesso: {len(tabela_apostas)}")

# 4. O DIA SEGUINTE: A ROTINA DE ESTORNO
print("\n" + "="*30)
print("🌞 DIA SEGUINTE: ROTINA DE CONCILIAÇÃO E ESTORNO")
print("="*30)

# Vamos comparar quem pagou vs quem tem bilhete
ids_com_bilhete = [d['id'] for d in tabela_apostas]

total_estornado = 0

for pagante in tabela_financeira:
    if pagante['id'] not in ids_com_bilhete:
        # Se pagou e não tá na lista de bilhetes -> ESTORNO
        lista_estorno.append(pagante)
        total_estornado += pagante['valor']

print(f"Relatório Final:")
print(f"✅ Apostas Válidas: {len(tabela_apostas)}")
print(f"❌ Apostas Falhas (Dinheiro entrou, bilhete não): {len(lista_estorno)}")
print(f"💸 Valor Total Devolvido aos clientes: R$ {total_estornado:,.2f}")

print("\nExemplo de cliente frustrado (na lista de estorno):")
if lista_estorno:
    print(lista_estorno[0])