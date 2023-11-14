import time
from Backtracking import Backtrack
from GeradorDeProblemas import GeradorDeProblemas

quant_rotas = 5
tam_conjunto = 3
dispersao = 0.7

result = GeradorDeProblemas.geracao_de_rotas(quant_rotas,tam_conjunto,dispersao)
print(result)

inicio = time.time()
checa_tempo = 0

while checa_tempo <= 30:
    for conjunto in result:
        print(" Backtrack")
        rotas_exemplo = conjunto
        num_caminhoes_exemplo = 4
        bactrack = Backtrack(rotas_exemplo, num_caminhoes_exemplo)
        bactrack.resolver()
        melhor_distribuicao_backtrack = bactrack.obter_melhor_distribuicao()
        bactrack.imprimir_melhor_distribuicao()
        print("Melhor distribuição:", melhor_distribuicao_backtrack)
        fim = time.time()
        checa_tempo = (fim -inicio)
        print(checa_tempo)




'''
a1) Utilizando o código do ‘gerador de problemas’ fornecido, medir o tempo de execução de
conjuntos de tamanho crescente, até atingir um tamanho T que não consiga ser resolvido em até
30 segundos pelo algoritmo. Este teste deve ser realizado para 3 caminhões e começando com 6
rotas. Na busca do tempo limite de 30 segundos, faça o teste com 10 conjuntos de cada tamanho,
contabilizando a média das execuções

Tempo limite de 30 segundos 
Número de caminhões fixo = 3
Início de quant_rotas = 6 
Faça o teste com 10 conjuntos de cada tamanho,contabilizando a média das execuções :
( o tamanho do conjunto de testes (ou seja, quantos conjuntos de rotas daquele
tamanho serão gerados) 
Ex : tamanho do conjunto 2, executa 10 vezes
    tamanho do conjunto 3, executa 10 vezes 
    tamanho do conjunto 4, executa 10 vezes

'''