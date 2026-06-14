# ============================================================
# PERGUNTA 3: Estudantes que trabalham têm maior probabilidade de evadir?
# Variáveis: Trabalha Atualmente (qualitativa nominal) + Status (qualitativa nominal)
# Medidas usadas:
#   - Posição: moda (variáveis qualitativas não usam média/mediana)
#   - Dispersão: covariância (relação entre duas variáveis)

# ============================================================

import pandas as pd
import numpy as np

# --- 1. Carregar os dados ---
df = pd.read_csv("dados.csv")

# --- 2. Contagem por grupo ---
# Contar quantos evadidos trabalham vs não trabalham
# Isso responde diretamente a pergunta
evadidos_trabalham = df[(df["Status"] == "Evadido") & (df["Trabalha Atualmente"] == "Sim")]
evadidos_nao_trabalham = df[(df["Status"] == "Evadido") & (df["Trabalha Atualmente"] == "Nao")]

total_trabalham = df[df["Trabalha Atualmente"] == "Sim"]
total_nao_trabalham = df[df["Trabalha Atualmente"] == "Nao"]

# --- 3. Moda ---
# Qual o status mais frequente entre quem trabalha?
moda_trabalham = df[df["Trabalha Atualmente"] == "Sim"]["Status"].mode()[0]

# Qual o status mais frequente entre quem não trabalha?
moda_nao_trabalham = df[df["Trabalha Atualmente"] == "Nao"]["Status"].mode()[0]

# --- 4. Covariância ---
# Para calcular covariância, precisamos transformar as colunas em números:
# Trabalha: Sim = 1, Não = 0
# Status: Evadido = 1, outros = 0
df["trabalha_num"] = df["Trabalha Atualmente"].map({"Sim": 1, "Nao": 0})
df["evadido_num"] = df["Status"].apply(lambda x: 1 if x == "Evadido" else 0)

# Covariância: se positiva, indica que quem trabalha tende mais a evadir
# Se negativa, quem trabalha tende menos a evadir
covariancia = df["trabalha_num"].cov(df["evadido_num"])

# --- 5. Taxa de evasão por grupo (porcentagem) ---
# Facilita a interpretação visual dos resultados
taxa_evasao_trabalham = (len(evadidos_trabalham) / len(total_trabalham)) * 100
taxa_evasao_nao_trabalham = (len(evadidos_nao_trabalham) / len(total_nao_trabalham)) * 100

# --- 6. Exibir resultados ---
print("=" * 55)
print("PERGUNTA 3: Estudantes que trabalham evadem mais?")
print("=" * 55)
print()
print("--- Contagem ---")
print(f"Evadidos que trabalham:     {len(evadidos_trabalham)}")
print(f"Evadidos que não trabalham: {len(evadidos_nao_trabalham)}")
print()
print("--- Medidas de Posição (Moda) ---")
print(f"Status mais comum entre quem trabalha:     {moda_trabalham}")
print(f"Status mais comum entre quem não trabalha: {moda_nao_trabalham}")
print()
print("--- Medida de Dispersão (Covariância) ---")
print(f"Covariância entre trabalho e evasão: {covariancia:.4f}")
print()
print("--- Taxa de Evasão por Grupo ---")
print(f"Taxa de evasão entre quem trabalha:     {taxa_evasao_trabalham:.1f}%")
print(f"Taxa de evasão entre quem não trabalha: {taxa_evasao_nao_trabalham:.1f}%")
print()

# --- 7. Interpretação da covariância ---
print("--- Interpretação ---")
if covariancia > 0:
    print("Covariância POSITIVA: quem trabalha tende a evadir mais.")
elif covariancia < 0:
    print("Covariância NEGATIVA: quem trabalha tende a evadir menos.")
else:
    print("Covariância ZERO: não há relação entre trabalhar e evadir.")
