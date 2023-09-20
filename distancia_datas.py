import datetime

def calcula_datas(lista_1:list, lista_2:list) -> int:
    """
    Parameters
    ----------
    lista_1 : list
        Lista contendo a data 1 no formato no formado ["DIA", "MES(numérico)", "ANO"]
    lista_2 : list
        Lista contendo a data 2 no formato no formado ["DIA", "MES(numérico)", "ANO"]

        DESCRIPTION. A função calcula_datas recebe duas listas contendo, cada uma, os telementos de uma data.
        A função converte essas datas para o formato datetime e calcula a diferença dos dias entre as datas.
    Returns
    -------
    int
        Retorna a diferença em dias entre as datas.

    A função só funcionará caso receba corretamente a data(no formato: "Dia1 de Mês1 de Ano1-Dia2 de Mês2 de Ano2").
    A seguir testes da função(O mesmo ocorre quando a função recebe um arquivo .txt com os respectivos textos):
    >>> calcula_datas(["31", "Agosto","2022"], ["18", "Setembro", "2023"])
    383
    
    >>> calcula_datas(["32", "Agosto","2022"], ["18", "Setembro", "2023"])
    Traceback (most recent call last):
    ...
    ValueError: Dia tem que estar entre 1 e 31!
    
    >>> calcula_datas(["31", "August","2022"], ["18", "Setembro", "2023"])
    Traceback (most recent call last):
    ...
    ValueError: O mês da primeira data não foi escrito corretamente

    >>> calcula_datas(["31", "Agosto","2022"], ["18", "September", "2023"])
    Traceback (most recent call last):
    ...
    ValueError: O mês da segunda data não foi escrito corretamente

    >>> calcula_datas(["31", "Agosto","2022"], ["31", "Setembro", "2023"])
    Traceback (most recent call last):
    ...
    ValueError: day is out of range for month
    
    """
    
    dia_1 = int(lista_1[0])
    dia_2 = int(lista_2[0])
   
    # Verificando se os dias estão no intervalo correto (1 a 31)
    if dia_1 > 31 or dia_1 < 1:
        raise ValueError("Dia tem que estar entre 1 e 31!")
    if dia_2 > 31 or dia_2 < 1:
        raise ValueError("Dia tem que estar entre 1 e 31!")
    
    # Analisando se o mês foi escrito corretamente
    if lista_1[1].isdigit()==False:
        raise ValueError("O mês da primeira data não foi escrito corretamente")
    if lista_2[1].isdigit()==False:
        raise ValueError("O mês da segunda data não foi escrito corretamente")
   
    # Juntando as strings restantes de cada lista em uma respectiva string, 
    # usando "-" como separador para adequar as strings para a conversão em data
    lista_1 = "-".join(lista_1)
    lista_2 = "-".join(lista_2)
    

    # Conversão das datas para o formato datetime (Dia-Mês-Ano)
    data_1 = datetime.datetime.strptime(lista_1, "%d-%m-%Y")
    data_2 = datetime.datetime.strptime(lista_2, "%d-%m-%Y")
    
    # Retorno da diferença de datas em dias absolutos
    return abs((data_2 - data_1).days)