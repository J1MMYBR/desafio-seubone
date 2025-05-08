# Desafio Análise de Dados da SeuBoné

## Bem-vindo!

Este repositório contém o desafio de Análise de Dados proposto pela SeuBoné, realizado por João Pedro Medeiros.

---

## Descrição do Desafio

1. **Carregamento e Armazenamento de Dados**

   * Efetue o download e carregue os arquivos CSV em um banco de dados (SQLite ou similar) de forma periódica.
   * Realize uma etapa de verificação de qualidade (vali­dação de tipos, remoção de registros inválidos, tratamento de nulos e outliers).
   * Gere logs ou relatórios básicos de quantos registros foram importados e quantos foram descartados.

2. **Construção de Visualizações (Dashboard)**

   * Crie gráficos ou painéis que respondam às seguintes perguntas:

     * **Top 3 produtos exportados por estado** nos anos de 2020 e 2021.
     * **Top 3 produtos importados por estado** nos anos de 2020 e 2021.
     * **Top 3 produtos exportados em cada mês de 2021 por estado**.

---

## Tecnologias e Dependências

* **Linguagem**: Python (versão >= 3.8)
* **Banco de Dados**: SQLite
* **Bibliotecas**:

  * `pandas>=2.2.3`
  * `plotly>=6.0.1`

---

## Instruções de Uso

1. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```
2. **Execute o arquivo principal**:

   ```bash
   python main.py
   ```
   * Isso vai ler os arquivos CSV em `inputs/`, filtrar e salvar em `database/`.
   * O dashboard será salvo em HTML na pasta `outputs/`.
3. **Visualize os resultados**:

   * Abra os arquivos `outputs/top3_imp.html`, `outputs/top3_exp.html` e `outputs/top3_exp_meses.html` no navegador.

---

## Estrutura do Repositório

```
├── inputs/                # CSVs brutos
├── database/              # Bancos SQLite gerados
├── outputs/               # Dashboards em HTML
├── dbManipulation.py      # Ingestão e qualidade de dados
├── genDashboard.py        # Geração dos gráficos em HTML
├── main.py                # Arquivo principal que executa todo o fluxo
├── requirements.txt       # Bibliotecas Python
└── README.md              # Documentação deste projeto
```

---

## Principais Funções
Estão listadas abaixo as funções-chave implementadas e seu propósito geral:

| Função                                                | Descrição                                                                                                                |
|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| `lerEFiltrar(input_path, output_path, table_name)`    | Lê um arquivo CSV de `input_path`, aplica filtros de qualidade e grava na tabela SQLite `table_name` em `output_path`.   |
| `printInfo(df)`                                       | Exibe informações gerais do DataFrame `df`, incluindo número de linhas, tipos de colunas e quantidade de valores nulos.  |
| `peneira(df, crit, desc)`                             | Filtra o DataFrame `df` com base no critério `crit` e registra `desc` para logs.                                         |
| `filtro(df)`                                          | Aplica filtros gerais (ex.: ano, UFs válidas) ao DataFrame `df`.                                                         |
| `filtroIMP(df)`                                       | Aplica filtros específicos para dados de importação no DataFrame `df`.                                                   |
| `printInvalidos()`                                    | Imprime ou registra as linhas descartadas por violarem regras de qualidade definidas.                                    |
| `carregarDBs()`                                       | Conecta e lê as tabelas SQLite em `database/`, retornando uma lista de DataFrames.                                       |
| `calcularTop3(df)`                                    | Agrupa o DataFrame `df` por ano, estado e produto, soma valores e retorna as 3 maiores entradas por estado/ano.          |
| `gerarESalvarTop3(top3_20, top3_21, fluxo, pathHtml)` | Gera gráficos comparativos de Top 3 (2020 vs 2021) para importação ou exportação e salva em HTML.                        |
| `gerarESalvarTopMes(df, pathHtml)`                    | Gera um gráfico com o Top 3 de produtos exportados por estado, mês a mês em 2021, e salva em HTML.                       |

---

## Links Úteis

- [Informações sobre layout de dados](https://www.gov.br/produtividade-e-comercio-exterior/pt-br/assuntos/comercio-exterior/estatisticas/base-de-dados-bruta
)
- [Repositório do desafio](https://github.com/ThiagoSViana/desafio-estagio-dados)

