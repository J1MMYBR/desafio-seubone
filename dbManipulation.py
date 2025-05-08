import sqlite3
import pandas as pd

UFS = [
    'AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS',
    'MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC',
    'SP','SE','TO'
]

INVALIDOS = {}

def lerEFiltrar(INPUT_PATH, OUTPUT_PATH, TABLE_NAME):

    df = pd.read_csv(
        INPUT_PATH,
        sep=';',
        quotechar='"'
        )
    
    df.columns = df.columns.str.strip()

    # converte CO_NCM e CO_URF em string e preenche zero a esquerda se precisar
    df['CO_NCM'] = df['CO_NCM'].astype(str).str.zfill(8)
    df['CO_URF'] = df['CO_URF'].astype(str).str.zfill(7)

    print("---- Antes do Filtro ----")
    printInfo(df)

    if 'IMP' in INPUT_PATH:
        df = filtro(df)
        df = filtroIMP(df)
    else:
        df = filtro(df)    

    print("---- Depois do Filtro ----")
    printInfo(df)
    printInvalidos()

    conn = sqlite3.connect(OUTPUT_PATH)
    df.to_sql(TABLE_NAME, conn, if_exists='replace', index=False)
    conn.close()

def printInfo(df):
    print("---- Informacoes ----\n")
    df.info()

    print("---- Valores Nulos ----\n")
    nulos = df.isnull().sum()
    print("Nulos por coluna:\n", nulos)

def peneira(df, crit, desc):
    antes = len(df)
    dfFiltrada = df[crit].copy()
    numRemovidos = antes - len(dfFiltrada)
    INVALIDOS[desc] = numRemovidos
    
    return dfFiltrada

def filtro(df):
    print("---- Iniciando Filtros ----\n")

    # filtrar mes
    crit = df['CO_MES'].between(1, 12)
    df = peneira(df, crit, "mes_invalido")

    #filtrar ano
    crit = df['CO_ANO'].isin([2020, 2021])
    df = peneira(df, crit, "ano_invalido")

    # filtrar UF
    crit = df['SG_UF_NCM'].isin(UFS)
    df = peneira(df, crit, "uf_invalida")

    # filtrar quantidade
    crit = df['QT_ESTAT'] >= 0
    df = peneira(df, crit, "qt_invalida")

    # filtrar peso
    crit = df['KG_LIQUIDO'] >= 0
    df = peneira(df, crit, "kg_invalido")

    # filtrar fob
    crit = df['VL_FOB'] >= 0
    df = peneira(df, crit, "fob_invalido")

    print("---- Fim Filtros ----\n")

    return df

def filtroIMP(df):
    print("---- Filtros IMP ----")

    # filtrar frete
    crit = df['VL_FRETE'] >= 0
    df = peneira(df, crit, "frete_invalido")

    #filtrar seguro
    crit = df['VL_SEGURO'] >= 0
    df = peneira(df, crit, "seguro_invalido")

    print("---- Fim Filtros IMP ----\n")

    return df

def printInvalidos():
    print(f"\n*** Quantidade de Linhas Invalidas: {sum(INVALIDOS.values())} ***")
    print("*** Linhas Invalidas Por Categoria ***")
    for desc, qnt in INVALIDOS.items():
        print(f"- {desc:25s}: {qnt}")

def main():
    INPUT_PATH = 'inputs/IMP_2021.csv'
    OUTPUT_PATH = 'database/IMP_2021.db'
    TABLE_NAME = 'IMP_2021'

    lerEFiltrar(INPUT_PATH, OUTPUT_PATH, TABLE_NAME)

if __name__ == "__main__":
    main()