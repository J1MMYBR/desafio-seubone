import pandas as pd
import plotly.express as px
import sqlite3
import os

def carregarDBs():
    dfs = []
    for tipo in ['IMP', 'EXP']:
        for ano in ['2020', '2021']:
            path = f'database/menor{tipo}_{ano}.db'
            if not os.path.exists(path):
                print(f"Banco de dados destino: {path} nao encontrado.")
                continue

            conn = sqlite3.connect(path)
            df = pd.read_sql_query(f'SELECT * FROM "menor{tipo}_{ano}"', conn)
            conn.close()
            dfs.append(df)
            # dfs[0] → IMP_2020
            # dfs[1] → IMP_2021
            # dfs[2] → EXP_2020
            # dfs[3] → EXP_2021
    return dfs

def calcularTop3(df):
    dfFiltrado = df.groupby(['CO_ANO', 'SG_UF_NCM', 'CO_NCM'], as_index=False)['QT_ESTAT'].sum()

    dfFiltrado = dfFiltrado.sort_values(
        ['SG_UF_NCM', 'QT_ESTAT'],
        ascending=[True, False]
    )

    top3 = dfFiltrado.groupby(['CO_ANO', 'SG_UF_NCM'], group_keys=False).head(3)

    return top3

def gerarESalvarTop3(top3_20, top3_21, fluxo, pathHtml):
    df = pd.concat([top3_20, top3_21], ignore_index=True)
    fig = px.bar(
        df,
        x='SG_UF_NCM',
        y='QT_ESTAT',
        color='CO_NCM',
        facet_col='CO_ANO',
        barmode='stack',
        template='simple_white',
        title=f'<b>Top 3 Produtos {fluxo} por Estado</b><br><sup>2020 vs 2021</sup>',
        labels={'SG_UF_NCM':'Estados','QT_ESTAT':'Quantidade (Mi)','CO_NCM':'Produto'},
        text=df['QT_ESTAT'].apply(lambda x: f'{x/1000000:,.2f}')
    )
    fig.update_xaxes(tickangle=-45, tickfont=dict(size=10))
    fig.update_yaxes(tickfont=dict(size=12))
    fig.write_html(pathHtml, auto_open=False)
    print(f'Grafico salvo em {pathHtml}')

def main():
    dfs = carregarDBs()

    top3s = [calcularTop3(df) for df in dfs]
    imp20 = top3s[0]
    imp21 = top3s[1]
    exp20 = top3s[2]
    exp21 = top3s[3]

    gerarESalvarTop3(imp20, imp21, 'Importação', 'top3_importacao.html')
    gerarESalvarTop3(exp20, exp21, 'Exportação', 'top3_exportacao.html')

if __name__ == '__main__':
    main()
