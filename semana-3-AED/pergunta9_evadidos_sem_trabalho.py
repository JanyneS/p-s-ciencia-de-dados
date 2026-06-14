# ============================================================
# PERGUNTA 9: Entre os evadidos que não trabalham, qual a faixa etária predominante?
# Variáveis: Idade (quantitativa discreta), filtrado por Status = Evadido
#            e Trabalha Atualmente = Não
# Medidas usadas:
#   - Posição: média, mediana, moda
#   - Dispersão: desvio padrão e variância
# OBSERVAÇÃO: aqui aplicamos DOIS filtros ao mesmo tempo (status E trabalho)
# ============================================================

import pandas as pd
import numpy as np

# --- 1. Carregar os dados ---
df = pd.read_csv("dados.csv")

# --- 2. Aplicar dois filtros ao mesmo tempo ---
# Queremos apenas linhas onde:
#   Status == "Evadido"   E   Trabalha Atualmente == "Nao"
# O símbolo & significa E (ambas as condições precisam ser verdadeiras)
filtro = (df["Status"] == "Evadido") & (df["Trabalha Atualmente"] == "Nao")
grupo = df[filtro]

idades = grupo["Idade"]

# --- 3. Medidas de Posição ---

# MÉDIA: idade média dos evadidos que não trabalham
media = idades.mean()

# MEDIANA: idade central desse grupo
mediana = idades.median()

# MODA: idade mais comum nesse grupo específico
moda = idades.mode()[0]

# --- 4. Medidas de Dispersão ---

# DESVIO PADRÃO: quanto as idades variam em torno da média
desvio_padrao = idades.std()

# VARIÂNCIA: dispersão total das idades nesse grupo
variancia = idades.var()

# Valor mínimo e máximo para entender o intervalo completo das idades
idade_min = idades.min()
idade_max = idades.max()

# --- 5. Exibir resultados ---
print("=" * 60)
print("PERGUNTA 9: Faixa etária dos evadidos que não trabalham")
print("=" * 60)
print(f"Total de pessoas nesse grupo: {len(idades)}")
print()
print("--- Medidas de Posição ---")
print(f"Média:   {media:.2f} anos")
print(f"Mediana: {mediana:.2f} anos")
print(f"Moda:    {moda} anos")
print(f"Mínimo:  {idade_min} anos")
print(f"Máximo:  {idade_max} anos")
print()
print("--- Medidas de Dispersão ---")
print(f"Desvio Padrão: {desvio_padrao:.2f} anos")
print(f"Variância:     {variancia:.2f} anos²")
print()

# --- 6. Comparação com o grupo total de evadidos ---
# Para entender se esse subgrupo é diferente do total de evadidos
todos_evadidos = df[df["Status"] == "Evadido"]["Idade"]
media_todos_evadidos = todos_evadidos.mean()

print("--- Comparação ---")
print(f"Média de idade de TODOS os evadidos:          {media_todos_evadidos:.2f} anos")
print(f"Média de idade dos evadidos sem trabalho:     {media:.2f} anos")
print()

# --- 7. Interpretação ---
print("--- Interpretação ---")
print(f"Entre os evadidos que não trabalham, a idade mais comum é {moda} anos.")
print(f"O desvio padrão de {desvio_padrao:.1f} anos indica que as idades")
if desvio_padrao < 4:
    print("são bastante homogêneas — este grupo tem perfil etário similar.")
else:
    print("variam bastante — este grupo inclui pessoas de diferentes faixas etárias.")
