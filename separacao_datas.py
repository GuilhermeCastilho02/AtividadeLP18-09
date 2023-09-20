def separa_datas(datas:str) -> list:
    """
    Parameters
    ----------
    datas : str
        string contendo as datas no formato "Dia1 de Mês1 de Ano1-Dia2 de Mês2 de Ano2"

        DESCRIPTION. A função separa_datas recebe uma string de datas e ordena as datas contidas nela em 2 listas.
        
    Returns
    -------
    list
        Retorna 2 listas de strings contendo a data 1 e a data 2 em cada uma, no formado ["DIA", "MES(numérico)", "ANO"]
    """

     # Separação da string contendo as duas datas para duas strings contendo cada data
    datas_sep = datas.split("-")
    data_str_1 = datas_sep[0].title() #'.title()' para garantir a funcionalidade, mesmo que o usuário não utilize letras maiúsculas no mês
    data_str_2 = datas_sep[1].title()
   
    # Cada data é dividida em uma lista de strings de única palavra, onde "de" é removido
    lista_data__1 = data_str_1.split(" ")
    lista_data__2 = data_str_2.split(" ")

    lista_data__1 = [x for x in lista_data__1 if x != "De"]
    lista_data__2 = [x for x in lista_data__2 if x != "De"]

    dic_meses = {
        "Janeiro": "1",
        "Fevereiro": "2",
        "Março": "3",
        "Abril": "4",
        "Maio": "5",
        "Junho": "6",
        "Julho": "7",
        "Agosto": "8",
        "Setembro": "9",
        "Outubro": "10",
        "Novembro": "11",
        "Dezembro": "12",  
        }

    # Conversão do Mês em formato de número
    for index in range(len(lista_data__1)):
        if lista_data__1[index] in dic_meses:
            lista_data__1[index]  = dic_meses[lista_data__1[index]]
        
    for index in range(len(lista_data__2)):
        if lista_data__2[index] in dic_meses:
            lista_data__2[index]  = dic_meses[lista_data__2[index]]
   
    # Retorna cada data como uma lista separada
    return lista_data__1, lista_data__2

