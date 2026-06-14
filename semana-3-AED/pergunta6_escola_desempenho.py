# ============================================================
# PERGUNTA 6: Existe correlação entre tipo de escola e desempenho?
# Variáveis: Escola Ensino Médio (qualitativa nominal) + Desempenho (quantitativa contínua)
# Medidas usadas:
#   - Posição: média e mediana do desempenho separadas por tipo de escola
#   - Dispersão: desvio padrão por grupo + covariância entre escola e desempenho
#
# ============================================================

import pandas as pd
import numpy as np

# --- 1. Carregar os dados ---
df = pd.read_csv("dados.csv")

# --- 2. Separar desempenho por tipo de escola ---
desemp_publica  = df[df["Escola Ensino Medio"] == "Publica"]["Desempenho"]
desemp_privada  = df[df["Escola Ensino Medio"] == "Privada"]["Desempenho"]

# --- 3. Medidas de Posição ---

# MÉDIA: nota média por tipo de escola
media_publica = desemp_publica.mean()
media_privada = desemp_privada.mean()

# MEDIANA: nota central por tipo de escola
mediana_publica = desemp_publica.median()
mediana_privada = desemp_privada.median()

# MODA: nota mais frequente por tipo de escola
moda_publica = desemp_publica.mode()[0]
moda_privada = desemp_privada.mode()[0]

# --- 4. Medidas de Dispersão ---

# DESVIO PADRÃO: quanto o desempenho varia dentro de cada grupo
dp_publica = desemp_publica.std()
dp_privada = desemp_privada.std()

# VARIÂNCIA: dispersão total do desempenho por grupo
var_publica = desemp_publica.var()
var_privada = desemp_privada.var()

# COVARIÂNCIA: relação entre tipo de escola e desempenho
# Convertemos escola para número para poder calcular
# Pública = 0, Privada = 1
df["escola_num"] = df["Escola Ensino Medio"].map({"Publica": 0, "Privada": 1})
covariancia = df["escola_num"].cov(df["Desempenho"])

# --- 5. Exibir resultados ---
print("=" * 60)
print("PERGUNTA 6: Tipo de escola influencia no desempenho?")
print("=" * 60)
print()
print(f"{'Escola':<10} {'Média':>8} {'Mediana':>9} {'Moda':>7} {'Desv. P.':>10} {'Variância':>11}")
print("-" * 58)
print(f"{'Pública':<10} {media_publica:>8.2f} {mediana_publica:>9.2f} {moda_publica:>7.1f} {dp_publica:>10.2f} {var_publica:>11.2f}")
print(f"{'Privada':<10} {media_privada:>8.2f} {mediana_privada:>9.2f} {moda_privada:>7.1f} {dp_privada:>10.2f} {var_privada:>11.2f}")
print()
print(f"Covariância (escola x desempenho): {covariancia:.4f}")
print()

# --- 6. Interpretação ---
print("--- Interpretação ---")
print(f"Escola pública: desempenho médio de {media_publica:.1f} pontos.")
print(f"Escola privada: desempenho médio de {media_privada:.1f} pontos.")
diferenca = media_privada - media_publica
if abs(diferenca) > 2:
    melhor = "Privada" if diferenca > 0 else "Pública"
    print(f"Diferença de {abs(diferenca):.1f} pontos — escola {melhor} tem desempenho maior.")
else:
    print("Diferença pequena — tipo de escola pode não ser fator determinante.")

print()
if covariancia > 0:
    print("Covariância positiva: escola privada tende a ter notas maiores.")
elif covariancia < 0:
    print("Covariância negativa: escola pública tende a ter notas maiores.")
