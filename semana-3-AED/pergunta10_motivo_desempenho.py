# ============================================================
# PERGUNTA 10: Existe relação entre o motivo da evasão e o desempenho?
# Variáveis: Motivo da Evasão (qualitativa nominal) + Desempenho (quantitativa contínua)
# Medidas usadas:
#   - Posição: média do desempenho para cada motivo de evasão
#   - Dispersão: desvio padrão por motivo + covariância entre motivo e desempenho
# OBSERVAÇÃO: para a covariância, o motivo é transformado em número (código)
# ============================================================

import pandas as pd
import numpy as np

# --- 1. Carregar os dados ---
df = pd.read_csv("dados.csv")

# --- 2. Filtrar apenas evadidos (só eles têm motivo preenchido) ---
evadidos = df[df["Status"] == "Evadido"].copy()

# --- 3. Medidas de Posição por motivo ---
# groupby agrupa as linhas pelo valor da coluna "Motivo da Evasao"
# e agg calcula as funções para cada grupo

# MÉDIA: nota média por motivo de evasão
media_por_motivo = evadidos.groupby("Motivo da Evasao")["Desempenho"].mean()

# MEDIANA: nota central por motivo
mediana_por_motivo = evadidos.groupby("Motivo da Evasao")["Desempenho"].median()

# CONTAGEM: quantos evadidos por motivo
contagem = evadidos.groupby("Motivo da Evasao")["Desempenho"].count()

# --- 4. Medidas de Dispersão por motivo ---

# DESVIO PADRÃO: quanto o desempenho varia dentro de cada grupo de motivo
dp_por_motivo = evadidos.groupby("Motivo da Evasao")["Desempenho"].std()

# VARIÂNCIA: dispersão total do desempenho por motivo
var_por_motivo = evadidos.groupby("Motivo da Evasao")["Desempenho"].var()

# COVARIÂNCIA: relação entre motivo (transformado em número) e desempenho
# Cada motivo recebe um código numérico para o cálculo
mapa_motivos = {
    "Baixo desempenho":       1,
    "Dificuldade financeira": 2,
    "Motivos pessoais":       3,
    "Trabalho":               4
}
evadidos["motivo_num"] = evadidos["Motivo da Evasao"].map(mapa_motivos)
covariancia = evadidos["motivo_num"].cov(evadidos["Desempenho"])

# --- 5. Exibir resultados ---
print("=" * 65)
print("PERGUNTA 10: Motivo da evasão x Desempenho acadêmico")
print("=" * 65)
print()
print(f"{'Motivo':<26} {'N':>4} {'Média':>7} {'Mediana':>9} {'Desv. P.':>10} {'Variância':>11}")
print("-" * 65)

for motivo in media_por_motivo.index:
    n    = contagem[motivo]
    med  = media_por_motivo[motivo]
    mdn  = mediana_por_motivo[motivo]
    # std pode ser NaN se só há 1 caso — tratamos com fillna
    dp   = dp_por_motivo.get(motivo, float('nan'))
    var  = var_por_motivo.get(motivo, float('nan'))
    dp_str  = f"{dp:.2f}"  if not pd.isna(dp)  else "—"
    var_str = f"{var:.2f}" if not pd.isna(var) else "—"
    print(f"{motivo:<26} {n:>4} {med:>7.2f} {mdn:>9.2f} {dp_str:>10} {var_str:>11}")

print()
print(f"Covariância (motivo x desempenho): {covariancia:.4f}")
print()

# --- 6. Identificar motivo com menor e maior desempenho ---
pior_motivo  = media_por_motivo.idxmin()
melhor_motivo = media_por_motivo.idxmax()

print("--- Interpretação ---")
print(f"Motivo com MENOR desempenho médio: '{pior_motivo}' ({media_por_motivo[pior_motivo]:.1f})")
print(f"Motivo com MAIOR desempenho médio: '{melhor_motivo}' ({media_por_motivo[melhor_motivo]:.1f})")
print()
print("Nota: estudantes que evadiram por 'Baixo desempenho' naturalmente")
print("tendem a ter notas menores, o que confirma a consistência dos dados.")
