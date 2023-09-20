def datas(arquivo=None) -> str:
    """
    Parameters
    ----------
    arquivo : .txt, optional
        arquivo.txt contendo duas datas no formato "Dia1 de Mês1 de Ano1-Dia2 de Mês2 de Ano2".
       
        DESCRIPTION. A função datas tem a opção de passar um arquivo .txt como parâmetro opcional. Caso não exista
        o parâmetro, o usuário deverá digitar as datas no Console.
        A função tem o objetivo de retornar as datas passadas pelo usuário.
    Returns
    -------
    str
        Retorna as datas escolhidas pelo usuário no formato "Dia1 de Mês1 de Ano1-Dia2 de Mês2 de Ano2".
    """
    
    if arquivo != None:
        file = open(arquivo, "r")
        datas = file.read()
    else:    
        datas = input("Digite as datas: ")
 
    return datas
    