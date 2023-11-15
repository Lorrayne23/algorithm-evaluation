import time
from Backtracking import Backtrack
from GeradorDeProblemas import GeradorDeProblemas

class ExecucaoAlgoritmos:
    def __init__(self):
        self.tempo_limite = 30
        self.dispersao = 0.7
        self.tempoDeExecucaoConjunto = []
        self.numCaminhoes = 3
        self.listaDeTamanhos = []
        self.listaRotas = []

    def executar_backtracking(self):
        tempo_execucao = 0
        tam_conjunto = 3
        quant_rotas = 6
        self.listaDeTamanhos.append(3)
        self.listaRotas.append(6)
        inicio_geral = time.time() # Tempo do começo de execução para controle de 30 segundos
        contaExecucao = 0
        while tempo_execucao<=30:
                inicio_execucao = time.time() # Tempo de início para soma de tempo de execução de cada tamanho
                for _ in range(10): # Roda 10 vezes com um tamanho X
                    print('range',_)
                    print('rotas quant',quant_rotas)
                    print('tamanho',tam_conjunto)
                    conjunto_teste = GeradorDeProblemas.geracao_de_rotas(quant_rotas, tam_conjunto,self.dispersao)
                    for conjunto in conjunto_teste:
                        bactrack = Backtrack(conjunto,self.numCaminhoes)
                        bactrack.resolver()
                        melhor_distribuicao_backtrack = bactrack.obter_melhor_distribuicao()
                        bactrack.imprimir_melhor_distribuicao()
                    contaExecucao+=1
                    if(contaExecucao==10):
                        ultimo_elemento_tamanho = self.listaDeTamanhos[-1]
                        novo_elemento_tamanho = ultimo_elemento_tamanho + 1
                        self.listaDeTamanhos.append(novo_elemento_tamanho)
                        tam_conjunto = self.listaDeTamanhos[-1]
                        ultimo_elemento_rotas = self.listaRotas[-1]
                        novo_elemento_rota = ultimo_elemento_rotas + 1
                        self.listaRotas.append(novo_elemento_rota)
                        quant_rotas = self.listaRotas[-1]
                        contaExecucao = 0
                fim = time.time() # Tempo final de execução de cada tamanho
                tempo_conjunto = (fim - inicio_execucao) # Calcula tempo de execução de conjunto
                self.tempoDeExecucaoConjunto.append(tempo_conjunto) # Adiciona em lista os tempos de cada tamanho
                tempo_execucao = (fim - inicio_geral) # Calcula tempo de inicio com tempo de fim para verificar segundos


            #tam_conjunto += 1

            #print('tempo execucao',tempo_execucao)






if __name__ == "__main__":
    execucao_algoritmos = ExecucaoAlgoritmos().executar_backtracking()
