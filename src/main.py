import pandas as pd
import argparse
import sys
import os

# 1. Módulo de Entrada (Input)
def carregar_dados(caminho_arquivo):
    """
    Lê o CSV de forma segura.
    """
    if not os.path.exists(caminho_arquivo):
        print(f"Erro: Arquivo não encontrado em: {caminho_arquivo}")
        sys.exit(1)
        
    try:
        df = pd.read_csv(caminho_arquivo)
        return df
    except Exception as e:
        print(f"Erro crítico ao abrir CSV: {e}")
        sys.exit(1)

# 2. Módulo de Processamento (Sua lógica aqui)
def processar_dados(df):
    """
    Processa vendas, top produtos e métricas de clientes (Top Cliente e Ticket Médio).
    """
    # Limpeza
    df['Quantidade'] = pd.to_numeric(df['Quantidade'], errors='coerce').fillna(0)
    df['Preco_Unitario'] = pd.to_numeric(df['Preco_Unitario'], errors='coerce').fillna(0)
    
    # Feature Engineering
    df['Subtotal'] = df['Quantidade'] * df['Preco_Unitario']

    # --- Métricas Gerais ---
    total_itens = int(df['Quantidade'].sum())
    faturamento_total = df['Subtotal'].sum()
    
    # --- Análise de Produtos ---
    top_produtos = (
        df.groupby('Produto')['Quantidade']
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    # --- Análise de Clientes ---
    gastos_por_cliente = df.groupby('ID_CLIENTE')['Subtotal'].sum()
    
    # Top Cliente
    if not gastos_por_cliente.empty:
        top_cliente_id = gastos_por_cliente.idxmax()
        top_cliente_valor = gastos_por_cliente.max()
    else:
        top_cliente_id = "N/A"
        top_cliente_valor = 0.0
    
    # Ticket Médio
    qtd_clientes_unicos = df['ID_CLIENTE'].nunique()
    ticket_medio = faturamento_total / qtd_clientes_unicos if qtd_clientes_unicos > 0 else 0

    # Retorno estruturado (Dicionário)
    return {
        "total_itens": total_itens,
        "faturamento": faturamento_total,
        "top_produtos": top_produtos,
        "top_cliente": (top_cliente_id, top_cliente_valor),
        "ticket_medio": ticket_medio,
        "total_clientes": qtd_clientes_unicos
    }

# 3. Módulo de Saída (Output)
def gerar_relatorio(dados):
    linha = "=" * 50
    print("\n" + linha)
    print("          RELATÓRIO DE VENDAS BYTESHOP (V2)")
    print(linha)
    
    print(f"Faturamento Total:       R$ {dados['faturamento']:,.2f}")
    print(f"Total de Itens:          {dados['total_itens']}")
    print(linha)
    
    id_top, valor_top = dados['top_cliente']
    print("MÉTRICAS DE CLIENTES:")
    print(f"• Total Clientes Únicos: {dados['total_clientes']}")
    print(f"• Ticket Médio (ARPU):   R$ {dados['ticket_medio']:,.2f}")
    print(f"• Top Cliente (ID {id_top}):    R$ {valor_top:,.2f}")
    
    print(linha)
    print("TOP 5 PRODUTOS (Qtd):")
    print("-" * 50)
    
    for produto, qtd in dados['top_produtos'].items():
        print(f"{produto:<30} | {int(qtd):>5} un")
    
    print(linha + "\n")

# 4. Orquestrador (Main)
def main():
    parser = argparse.ArgumentParser(description="Analytics ByteShop")
    # Argumento opcional: Se não passar nada, usa o seu caminho padrão
    parser.add_argument('arquivo', nargs='?', type=str, 
                        default=r"C:\Users\mchar\OneDrive\Projetos\byteshop_analytics\data\vendas.csv",
                        help='Caminho do CSV')
    
    args = parser.parse_args()
    
    print(f"Processando arquivo: {args.arquivo}...")
    
    # Fluxo de execução
    df = carregar_dados(args.arquivo)
    dados_processados = processar_dados(df)
    gerar_relatorio(dados_processados)

if __name__ == "__main__":
    main()