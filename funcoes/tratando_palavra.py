def tratar(palavra):

    import unicodedata


    processamento = unicodedata.normalize("NFD", palavra)

    processamento = processamento.encode("ascii", "ignore")

    processamento = processamento.decode("utf-8")

    processamento = processamento.lower()

    processamento = processamento.replace(" ", "")

    return processamento
