import pandas as pd
import csv

exp_20 = pd.read_csv(
    'inputs/EXP_2020.csv',
    sep=';',
    quotechar='"',
    dtype=str,
    nrows=50_000,
    low_memory=False
    )

exp_20.to_csv(
    'inputs/menorEXP_2020.csv',
    sep=';',
    index=False,
    quotechar='"',
    quoting=csv.QUOTE_ALL
    )

exp_21 = pd.read_csv(
    'inputs/EXP_2021.csv',
    sep=';',
    quotechar='"',
    dtype=str,
    nrows=50_000,
    low_memory=False
    )

exp_21.to_csv(
    'inputs/menorEXP_2021.csv',
    sep=';',
    index=False,
    quotechar='"',
    quoting=csv.QUOTE_ALL
    )

imp_20 = pd.read_csv(
    'inputs/IMP_2020.csv',
    sep=';',
    quotechar='"',
    dtype=str,
    nrows=50_000,
    low_memory=False
    )

imp_20.to_csv(
    'inputs/menorIMP_2020.csv',
    sep=';',
    index=False,
    quotechar='"',
    quoting=csv.QUOTE_ALL
    )

imp_21 = pd.read_csv(
    'inputs/IMP_2021.csv',
    sep=';',
    quotechar='"',
    dtype=str,
    nrows=50_000,
    low_memory=False
    )

imp_21.to_csv(
    'inputs/menorIMP_2021.csv',
    sep=';',
    index=False,
    quotechar='"',
    quoting=csv.QUOTE_ALL
    )

# apenas um algoritmo auxiliar. cria outros arquivos .csv com 50k linhas para melhor manipulacao em testes

print(f"Operacao concluida com sucesso, 4 arquivos com {len(imp_20)} linhas salvas.")
