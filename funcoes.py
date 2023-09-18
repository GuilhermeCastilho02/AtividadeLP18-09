import datetime
import doctest

def countdate(arquivo=None):
    """
    Parameters
    ----------
    arquivo : .txt, optional
        DESCRIPTION. A função countdate tem a opção de passar um arquivo .txt como parâmetro opcional. Caso não não exista
        o parâmetro, o usuário deverá digitar as datas no Console.
        A função tem o objetivo de calcular a diferença dos dias da data passada no formato 
        "Dia1 de Mês1 de Ano1-Dia2 de Mês2 de Ano2".
    Returns
    -------
    TYPE int
        DESCRIPTION Retorna a diferença entre as datas.

    """
    # Tenta dar a opção de passar um arquivo com as datas
    if arquivo != None:
        conteudo = open(arquivo, "r")
        data = conteudo.read()
    else:    
        data = input("Digite as datas: ")

    # Separação das duas datas passadas
    datas = data.split("-")
    date_str1 = datas[0]
    date_str2 = datas[1]
    date_str1.upper()
    date_str2.upper()
    tmp_list_1 = date_str1.split(" ")
    tmp_list_2 = date_str2.split(" ")
    # Cada data é dividida em palavras separadas, onde "de" é removido
    tmp_list_1 = [x for x in tmp_list_1 if x != "de"]
    tmp_list_2 = [x for x in tmp_list_2 if x != "de"]
    dict_date = {
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
    for i in range(len(tmp_list_1)):
        if tmp_list_1[i] in dict_date:
            tmp_list_1[i]  = dict_date[tmp_list_1[i] ]
    for i in range(len(tmp_list_2)):
        if tmp_list_2[i] in dict_date:
            tmp_list_2[i]  = dict_date[tmp_list_2[i] ]
    tmp_list_2 = "-".join(tmp_list_2)
    tmp_list_1 = "-".join(tmp_list_1)
    # Conversão das datas para o formato datetime (Dia-Mês-Ano)
    d1 = datetime.datetime.strptime(tmp_list_1, "%d-%m-%Y")
    d2 = datetime.datetime.strptime(tmp_list_2, "%d-%m-%Y")
    # Retorno da diferença de datas em dias absolutos
    return abs((d2 - d1).days)


    


