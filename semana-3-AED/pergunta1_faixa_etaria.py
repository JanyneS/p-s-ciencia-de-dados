# ============================================================
# PERGUNTA 1: Existe uma faixa etária predominante entre os evadidos?
# Variáveis: Idade (quantitativa discreta) + Status (qualitativa nominal)
# Medidas usadas:
#   - Posição: média, mediana, moda
#   - Dispersão: desvio padrão, variância
# ============================================================

import pandas as pd
import numpy as np
from scipy import stats

# --- 1. Carregar os dados ---
# O arquivo dados.csv deve estar na mesma pasta que este script
df = pd.read_csv("dados.csv")

# --- 2. Filtrar apenas os evadidos ---
# Criamos um novo dataframe só com as linhas onde Status == "Evadido"
evadidos = df[df["Status"] == "Evadido"]

# Pegamos só a coluna de Idade dos evadidos
idades = evadidos["Idade"]

# --- 3. Medidas de Posição ---

# Média: soma de todas as idades dividida pelo total de evadidos
media = idades.mean()

# Mediana: valor central quando as idades estão em ordem crescente
mediana = idades.median()

# Moda: idade que aparece com maior frequência entre os evadidos
moda = idades.mode()[0]  # [0] pega o primeiro valor caso haja empate

# --- 4. Medidas de Dispersão ---

# Desvio Padrão: quanto as idades se afastam da média em média
# Quanto mais próximo de 0, mais homogêneas são as idades
desvio_padrao = idades.std()

# Variância: é o desvio padrão ao quadrado
# Mede a dispersão total, mas em unidade ao quadrado (anos²)
variancia = idades.var()

# --- 5. Exibir os resultados ---
print("=" * 50)
print("PERGUNTA 1: Faixa etária predominante dos evadidos")
print("=" * 50)
print(f"Total de evadidos analisados: {len(idades)}")
print()
print("--- Medidas de Posição ---")
print(f"Média:   {media:.2f} anos")
print(f"Mediana: {mediana:.2f} anos")
print(f"Moda:    {moda} anos")
print()
print("--- Medidas de Dispersão ---")
print(f"Desvio Padrão: {desvio_padrao:.2f} anos")
print(f"Variância:     {variancia:.2f} anos²")
print()

# --- 6. Interpretação ---
print("--- Interpretação ---")
print(f"A idade média dos evadidos é {media:.1f} anos.")
print(f"A idade mais comum (moda) entre os evadidos é {moda} anos.")
print(f"O desvio padrão de {desvio_padrao:.1f} anos indica que as idades")
print(f"variam em média {desvio_padrao:.1f} anos em torno da média.")
