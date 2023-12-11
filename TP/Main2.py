import time
import signal
from GeradorDeProblemas import GeradorDeProblemas
from Backtracking import  Backtrack
from AlgoritmoGuloso import Greedy
from DivisaoConquista import MergeSort
from ProgramacaoDinamica import distribuir_rotas

class ExecucaoAlgoritmos():
    def __init__(self,conjunto_rotas):
        self.numCaminhoes = 3
        self.tamanho_conjunto = 10
        self.dispersao = 0.7
        self.tempo_maximo = 30
        self.conjunto_rotas = conjunto_rotas
        self.tempoDeExecucaoBacktracking = []
        self.tempoDeExecucaoGulosoEstrategia1 = []
        self.tempoDeExecucaoGulosoEstrategia2 = []
        self.tempoDeExecucaoDivisaoConquista = []
        self.tempoDeExecucaoProgamacaoDinamica = []

    def execucaoBacktracking(self):

                inicio_execucao = time.time()
                bactrack = Backtrack(conjunto_rotas, self.numCaminhoes)
                bactrack.resolver()
                melhor_distribuicao_backtrack = bactrack.obter_melhor_distribuicao()
                imprimir_distribuicao = bactrack.imprimir_melhor_distribuicao()
                fim = time.time()  # Tempo final de execução
                tempo_conjunto = (fim - inicio_execucao)  # Calcula o tempo de execução do conjunto
                self.tempoDeExecucaoBacktracking.append(tempo_conjunto)  # Adiciona em lista os tempos
                mediaTempo = sum(self.tempoDeExecucaoBacktracking) / len(self.tempoDeExecucaoBacktracking) # Calcula média
                return mediaTempo


    def execucaoGulosoEstrategia1(self):
            inicio_execucao = time.time()
            estrategia1 = Greedy(self.numCaminhoes, conjunto_rotas)
            estrategia1.distribuir_rotas_menor()
            estrategia1.exibir_distribuicao('menor')
            fim = time.time()  # Tempo final de execução de cada tamanho
            tempo_conjunto = (fim - inicio_execucao)  # Calcula o tempo de execução do conjunto
            self.tempoDeExecucaoGulosoEstrategia1.append(tempo_conjunto)  # Adiciona em lista de tempos
            mediaTempo = sum(self.tempoDeExecucaoGulosoEstrategia1) / len(self.tempoDeExecucaoGulosoEstrategia1) # Calcula média
            return mediaTempo



    def execucaoGulosoEstrategia2(self):
            inicio_execucao = time.time()
            estrategia2 = Greedy(self.numCaminhoes, conjunto_rotas)
            estrategia2.distribuir_rotas_agrupamento()
            estrategia2.exibir_distribuicao('agrupamento')
            fim = time.time()  # Tempo final de execução
            tempo_conjunto = (fim - inicio_execucao)  # Calcula o tempo de execução do conjunto
            self.tempoDeExecucaoGulosoEstrategia2.append(tempo_conjunto)  # Adiciona em lista os tempos
            mediaTempo = sum(self.tempoDeExecucaoGulosoEstrategia2) / len(self.tempoDeExecucaoGulosoEstrategia2)
            return mediaTempo


    def execucaoDivisaoConquista(self):
            inicio_execucao = time.time()
            divisaoConquista = MergeSort(conjunto_rotas, self.numCaminhoes)
            divisaoConquista.distribuir_quilometragem()
            divisaoConquista.imprimir_distribuicao()
            fim = time.time()  # Tempo final de execução de cada tamanho
            tempo_conjunto = (fim - inicio_execucao)  # Calcula o tempo de execução do conjunto
            self.tempoDeExecucaoDivisaoConquista.append(tempo_conjunto)  # Adiciona em lista os tempos
            mediaTempo = sum(self.tempoDeExecucaoDivisaoConquista)/len(self.tempoDeExecucaoDivisaoConquista)
            return mediaTempo

    def execucaoProgramacaoDinamica(self):
            inicio_execucao = time.time()
            distribuir_rotas(conjunto_rotas,self.numCaminhoes)
            fim = time.time()  # Tempo final de execução de cada tamanho
            tempo_conjunto = (fim - inicio_execucao)  # Calcula o tempo de execução do conjunto
            self.tempoDeExecucaoProgamacaoDinamica.append(tempo_conjunto)  # Adiciona em lista os tempos
            mediaTempo = sum(self.tempoDeExecucaoProgamacaoDinamica) / len(self.tempoDeExecucaoProgamacaoDinamica)
            return mediaTempo




if __name__ == "__main__":
    #conjunto_rotas = [40,36,38,29,32,28,31,35,31,30,32,30,29,39,35,38,39,35,32,38,32,33,29,33,29,39,28]
    conjunto_rotas =[32,51,32,43,42,30,42,51,43,51,29,25,27,32,29,55,43,29,32,44,55,29,53,30,24,27]

    execucao = ExecucaoAlgoritmos(conjunto_rotas)
    mediaTempoBacktacking= execucao.execucaoBacktracking()
    print('Média de execução Backtracking : ', mediaTempoBacktacking)

    mediaTempoGulosoEstrategia1 = execucao.execucaoGulosoEstrategia1()
    print('Média de execução Guloso Estratégia 1 : ', mediaTempoGulosoEstrategia1)

    mediaTempoGulosoEstrategia2 = execucao.execucaoGulosoEstrategia2()
    print('Média de execução Guloso Estratégia 2 : ', mediaTempoGulosoEstrategia2)

    mediaTempoDivisaoConquista = execucao.execucaoDivisaoConquista()
    print('Média de execução Divisião por Conquista : ', mediaTempoDivisaoConquista)

    mediaTempoProgramacaoDinamica = execucao.execucaoProgramacaoDinamica()
    print('Média de execução Programação Dinâmica : ', mediaTempoProgramacaoDinamica)

