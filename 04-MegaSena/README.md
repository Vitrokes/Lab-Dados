# 🎱 Simulação de Gargalo de Dados - Mega da Virada 2025/2026

Este projeto simula o cenário técnico que causou o adiamento do sorteio da Mega da Virada.
Utilizando Python, reproduzimos problemas de **Concorrência**, **Filas (Queues)** e **Consistência de Dados**.

## 🛠️ O que foi simulado:

1.  **Race Conditions:** O que acontece quando Apps e Lotéricas tentam gravar no mesmo banco ao mesmo tempo.
2.  **Gargalo de I/O (Input/Output):** Simulamos um banco de dados com capacidade de escrita menor que a demanda de entrada (120k req/s na vida real vs capacidade limitada).
3.  **Conciliação Financeira:** Script que detecta discrepâncias entre o "Dinheiro que entrou" (Gateway) e "Apostas Gravadas" (Database), gerando a necessidade de estornos.

## 📉 Resultados da Simulação:
O script `simulacao_estouro.py` demonstrou que, sob carga excessiva, o sistema aceita a conexão (pagamento), mas falha na persistência (gravação), resultando em:
* Timeouts de conexão.
* Perda de dados em memória volátil.
* Necessidade de rotinas de auditoria pós-evento (Batch Processing).

---
*Estudo de Ciência de Dados.*