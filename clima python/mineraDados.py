from pathlib import Path

import numpy as np
import pandas as pd

from clima import clima
from principalclima import criar_clima

# Arquivo padrao que armazenara os dados brutos a serem minerados.
CSV_BASE = Path("base.csv")


def carregar_dataframe(caminho: Path) -> pd.DataFrame:
    """
    Usa pandas para ler todo o CSV de uma vez e padronizar os nomes das colunas.

    - Verifica antes se o arquivo existe para evitar excecao de IO.
    - pandas.read_csv consegue tratar a leitura em blocos, aplicar encoding latin-1,
      pular espacos extras e criar colunas com nomes significativos.
    - Dropamos quaisquer linhas que contenham valores ausentes para manter a integridade
      dos aggregadores posteriores.
    """
    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo {caminho} nao encontrado.")

    df = pd.read_csv(
        caminho,
        header=None,
        names=["ano", "mes", "temperatura", "precipitacao"],
        skipinitialspace=True,
        encoding="latin-1",
    )
    return df.dropna()


def contar_com_numpy(serie: pd.Series) -> dict[str, int]:
    """
    Converte a Series do pandas em um array numpy e retorna os valores unicos
    com suas frequencias absolutas.

    numpy.unique eh rapido para arrays e nos permite evitar loops manuais sobre
    cada linha do DataFrame; o uso de numpy complementa os recursos de pandas.
    """
    valores, contagens = np.unique(serie.to_numpy(), return_counts=True)
    return dict(zip(valores.tolist(), contagens.tolist()))


def proporcao(contador: dict[str, int]) -> dict[str, float]:
    """
    Recebe um contador simples (string -> total) e calcula a proporcao percentual
    (com uma casa decimal) de cada categoria sobre o total.
    """
    if not contador:
        return {}
    valores = np.array(list(contador.values()), dtype=float)
    total = valores.sum()
    proporcoes = np.round(valores / total * 100, 1)
    return dict(zip(contador.keys(), proporcoes.tolist()))


def formatar_contagem(contador: dict[str, int]) -> str:
    """
    Representa o dicionario de frequencias em uma string legivel para impressao.
    """
    return ", ".join(f"{chave}: {valor}" for chave, valor in contador.items())


def instanciar_climas_unicos(df: pd.DataFrame) -> list[clima]:
    """
    Percorre cada tupla (ano, mes, temperatura, precipitacao) e usa o helper
    disponibilizado em principalclima para criar objetos clima, mantendo
    apenas instancias unicas via comparacao de ano e mes.
    """
    registros = []
    for ano, mes, temperatura, precipitacao in df.itertuples(index=False, name=None):
        registro = criar_clima(ano, mes, temperatura, precipitacao)
        if registro not in registros:
            registros.append(registro)
    return registros


def imprimir_resumo(df: pd.DataFrame, registros_unicos: list[clima]) -> None:
    """
    Consolida e imprime o resumo geral:
      * quantidade total de linhas lidas
      * quantidade de objetos clima unicos instanciados
      * distribuicao geral de temperaturas e precipitacoes (valores brutos)
      * resumo agrupado por ano, com contagens e porcentagens calculadas por numpy
    """
    total_registros = len(df)
    temperaturas_globais = contar_com_numpy(df["temperatura"])
    precipitacoes_globais = contar_com_numpy(df["precipitacao"])

    print(f"{total_registros} linhas processadas do arquivo {CSV_BASE.name}")
    print(f"{len(registros_unicos)} registros unicos instanciados via clima")
    print("Distribuicao geral:")
    print(f"  Temperaturas: {formatar_contagem(temperaturas_globais)}")
    print(f"  Precipitacoes: {formatar_contagem(precipitacoes_globais)}")

    print("\nResumo por ano:")
    for ano, grupo in df.groupby("ano", sort=True):
        temp_contagem = contar_com_numpy(grupo["temperatura"])
        precip_contagem = contar_com_numpy(grupo["precipitacao"])
        print(f"  {ano} ({len(grupo)} registros)")
        print(f"    Temperaturas: {formatar_contagem(temp_contagem)}")
        print(f"    Precipitacoes: {formatar_contagem(precip_contagem)}")
        print(f"    Temperaturas (%) : {proporcao(temp_contagem)}")


def main() -> None:
    """
    Entrypoint do script: carrega os dados, instancia os objetos, imprime o resumo.
    """
    try:
        df = carregar_dataframe(CSV_BASE)
    except FileNotFoundError as exc:
        print(exc)
        return

    if df.empty:
        print("Nenhum dado foi carregado.")
        return

    registros_unicos = instanciar_climas_unicos(df)
    imprimir_resumo(df, registros_unicos)


if __name__ == "__main__":
    main()
