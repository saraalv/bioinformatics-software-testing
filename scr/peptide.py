def concatenacion_peptidos(peptido1, peptido2):
    peptidos = [
        "A", "R", "N", "D", "C", "Q", "E", "G", "H", "I",
        "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"
    ]

    peptido1, peptido2 = peptido1.upper(), peptido2.upper()

    for i in peptido1:
        if i not in peptidos:
            raise ValueError(
                "Introduzca un código de aminoácidos válido en peptido1"
            )

    for j in peptido2:
        if j not in peptidos:
            raise ValueError(
                "Introduzca un código de aminoácidos válido en peptido2"
            )

    return peptido1 + peptido2


def polyh(peptido, num):
    peptidos = [
        "A", "R", "N", "D", "C", "Q", "E", "G", "H", "I",
        "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"
    ]

    peptido = peptido.upper()

    for i in peptido:
        if i not in peptidos:
            raise ValueError(
                "Introduzca un código de aminoácidos válido"
            )

    return peptido + "H" * num
