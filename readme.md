# 📊 ByteShop Analytics

> Ferramenta de CLI modular para análise de performance de vendas e geração de relatórios gerenciais.

---

## 📝 Sobre o Projeto

A **ByteShop**, uma startup de eletrônicos, necessitava otimizar a visualização de suas vendas diárias.  
Este projeto consiste em uma automação desenvolvida em **Python** que processa dados brutos de vendas (CSV), realiza limpeza, *feature engineering* e cálculos estatísticos para entregar insights rápidos e assertivos à equipe de marketing.

---

## ✅ Checklist de Conformidade (Requisitos)

### 1. Requisitos Funcionais (Métricas)

- ✅ **Volume Total:** Cálculo exato da quantidade de itens vendidos.  
- ✅ **Faturamento:** Soma monetária total das transações.  
- ✅ **Top 5 Produtos:** Ranking dos itens com maior saída.  

#### 🌟 Bônus (Extras)

- **Ticket Médio (ARPU):** Valor médio gasto por cliente único.  
- **Top Cliente:** Identificação do cliente com maior volume financeiro de compras.

---

### 2. Restrições Técnicas (Tech Constraints)

- ✅ **Modularidade:** Código dividido em camadas — IO, Core e View.  
- ✅ **Pandas:** Motor principal de manipulação de dados.  
- ✅ **CLI (Linha de Comando):** Implementado com `argparse`.  
- ✅ **Dependências:** Arquivo `requirements.txt` incluso.

---

## 📂 Estrutura do Projeto

```text
.
├── data/
│   └── vendas.csv        # Dataset de exemplo (Entrada)
├── src/
│   └── main.py           # Script principal (Modularizado)
├── requirements.txt      # Lista de dependências
└── README.md             # Documentação do projeto
```

---

## 🚀 Como Executar

### 1. Instalação e Pré-requisitos

Certifique-se de ter Python 3.x. Instale as dependências:

```bash
pip install -r requirements.txt
```

---

### 2. Execução via CLI

#### **Opção A — Modo Padrão**

O script buscará automaticamente `data/vendas.csv`.

```bash
python src/main.py
```

#### **Opção B — Arquivo Personalizado**

Aponte para qualquer arquivo CSV:

```bash
python src/main.py "C:\Caminho\Para\Seu\Arquivo.csv"
```

---

## 📊 Especificação do CSV (Schema)

| Coluna         | Tipo        | Descrição                                  |
|----------------|-------------|----------------------------------------------|
| ID_CLIENTE     | Int/String  | Identificador único do comprador             |
| Produto        | String      | Nome do item                                 |
| Quantidade     | Int         | Quantidade de itens na transação             |
| Preco_Unitario | Float       | Preço unitário do produto                    |

---

---

## 👨‍💻 Autor

**Maikon Silva**
