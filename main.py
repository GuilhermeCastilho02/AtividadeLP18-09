from recebe_datas import datas
from separacao_datas import separa_datas
from distancia_datas import calcula_datas

datas_inicial = datas("AtividadeLP18-09\data_atividade.txt")

lista_data_1, lista_data_2 = separa_datas(datas_inicial)

resultado = calcula_datas(lista_data_1, lista_data_2)

print(resultado)