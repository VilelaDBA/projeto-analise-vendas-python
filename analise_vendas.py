# Projeto: Análise de Vendas com Python e Pandas
# Autor: Aline Vilela
# Descrição: Projeto de análise de vendas simuladas, incluindo cálculo de faturamento,
# identificação do produto mais vendido, faturamento por categoria e região, ticket médio
# e visualizações gráficas com valores em reais para interpretação clara.

# =========================
# 0. Importando bibliotecas
# =========================
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick  # Para formatar valores monetários

# =========================
# 1. Criando os dados manualmente
# =========================
vendas_dados = {
    "Data": [
        "2025-08-27","2025-08-27","2025-08-28","2025-08-28",
        "2025-08-30","2025-08-30","2025-09-01","2025-09-01",
        "2025-09-01","2025-09-02"
    ],
    "Cliente": [
        "João Silva","Aline Vilela","Melissa Cardoso","Luiz Antonio",
        "Maria Souza","Carlos Pereira","João Silva","Aline Vilela",
        "Melissa Cardoso","Luiz Antonio"
    ],
    "Produto": [
        "Notebook","Mochila","Camiseta","Smartphone",
        "Tênis","Relógio","Fone de Ouvido","Geladeira",
        "Cadeira","Livro"
    ],
    "Categoria": [
        "Eletrônicos","Acessórios","Vestuário","Eletrônicos",
        "Vestuário","Acessórios","Eletrônicos","Eletrônicos",
        "Móveis","Educacional"
    ],
    "Quantidade": [1,2,3,1,2,1,2,1,1,4],
    "Preco": [2599.99,129.90,49.90,1899.99,199.90,299.90,89.90,1599.00,349.90,59.90],
    "Regiao": [
        "Sudeste","Sul","Sudeste","Nordeste",
        "Sudeste","Sul","Nordeste","Sudeste",
        "Sul","Sudeste"
    ]
}

# Criando o DataFrame
vendas_df = pd.DataFrame(vendas_dados)

# Convertendo coluna "Data" para datetime
vendas_df["Data"] = pd.to_datetime(vendas_df["Data"])

# Criando coluna de faturamento
vendas_df["Faturamento"] = vendas_df["Quantidade"] * vendas_df["Preco"]

# =========================
# 2. Análises principais
# =========================

# Faturamento total
faturamento_total = vendas_df["Faturamento"].sum()
print(f"Faturamento Total: R$ {faturamento_total:,.2f}")

# Produto mais vendido (quantidade)
produto_mais_vendido = vendas_df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False).head(1)
print("\nProduto mais vendido (quantidade):")
print(produto_mais_vendido)

# Faturamento por categoria
faturamento_categoria = vendas_df.groupby("Categoria")["Faturamento"].sum().sort_values(ascending=False)
print("\nFaturamento por categoria:")
print(faturamento_categoria)

# Faturamento por região
faturamento_regiao = vendas_df.groupby("Regiao")["Faturamento"].sum().sort_values(ascending=False)
print("\nFaturamento por região:")
print(faturamento_regiao)

# Ticket médio
ticket_medio = vendas_df["Faturamento"].mean()
print(f"\nTicket médio por venda: R$ {ticket_medio:,.2f}")

# =========================
# 3. Visualizações Profissionais
# =========================

# Função para formatar valores em R$ nos gráficos
def formatar_moeda(ax):
    ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('R$ {x:,.0f}'))

# 3.1 Faturamento por Categoria
plt.figure(figsize=(8,5))
ax = faturamento_categoria.plot(kind="bar", color="#5DADE2")  # azul harmônico
plt.title("Faturamento por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Faturamento")
plt.xticks(rotation=45)
formatar_moeda(ax)
plt.tight_layout()
plt.show()

# 3.2 Faturamento por Região
plt.figure(figsize=(6,4))
ax = faturamento_regiao.plot(kind="bar", color="#58D68D")  # verde suave
plt.title("Faturamento por Região")
plt.xlabel("Região")
plt.ylabel("Faturamento")
plt.xticks(rotation=0)
formatar_moeda(ax)
plt.tight_layout()
plt.show()

# 3.3 Quantidade vendida por Produto
quantidade_produto = vendas_df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)
plt.figure(figsize=(8,5))
ax = quantidade_produto.plot(kind="bar", color="#F1948A")  # vermelho suave
plt.title("Quantidade Vendida por Produto")
plt.xlabel("Produto")
plt.ylabel("Quantidade")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# =========================
# 4. Insights
# =========================
print("\nInsights:")
print("- A categoria Eletrônicos tem o maior faturamento, mostrando forte impacto financeiro.")
print("- O produto mais vendido em quantidade foi:", produto_mais_vendido.index[0])
print("- A região Sudeste lidera o faturamento total, indicando mercado estratégico.")
