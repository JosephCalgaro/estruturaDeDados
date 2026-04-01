from clima import clima


def criar_clima(ano, mes, temperatura, precipitacao):
    # garante que todos os campos sejam strings antes de aplicar strip
    return clima(
        str(ano).strip(),
        str(mes).strip(),
        str(temperatura).strip(),
        str(precipitacao).strip(),
    )


def criar_clima_a_partir_de(linha):
    partes = [p.strip() for p in linha.split(",")]
    return criar_clima(*partes[:4])


def demonstrar_exemplos():
    exemplos = [
        "2020, Janeiro, Quente, muita",
        "2020, Janeiro, Frio, pouca",
    ]
    registros = []
    for linha in exemplos:
        obj_clima = criar_clima_a_partir_de(linha)
        if obj_clima not in registros:
            registros.append(obj_clima)

    for c in registros:
        print(c)


if __name__ == "__main__":
    demonstrar_exemplos()
