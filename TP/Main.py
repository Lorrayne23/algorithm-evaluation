import time
import signal
from GeradorDeProblemas import GeradorDeProblemas
from Backtracking import  Backtrack
from AlgoritmoGuloso import Greedy
from DivisaoConquista import MergeSort
from ProgramacaoDinamica import distribuir_rotas

class ExecucaoAlgoritmos:
    def __init__(self):
        self.numCaminhoes = 3
        self.tamanho_conjunto = 10
        self.dispersao = 0.7
        self.tempo_maximo = 30
        self.tempoDeExecucaoBacktracking = []
        self.tempoDeExecucaoGulosoEstrategia1 = []
        self.tempoDeExecucaoGulosoEstrategia2 = []
        self.tempoDeExecucaoDivisaoConquista = []
        self.tempoDeExecucaoProgamacaoDinamica = []

    def execucaoBacktracking(self):
        def handler(signum, frame):
            raise TimeoutError("Tempo máximo de execução atingido")

        signal.signal(signal.SIGALRM, handler)
        signal.alarm(self.tempo_maximo)

        try:
            quantRotas = 6
            while True:
                conjunto_teste = GeradorDeProblemas.geracao_de_rotas(quantRotas, self.tamanho_conjunto, self.dispersao)
                inicio_execucao = time.time()
                for conjunto in conjunto_teste:
                    bactrack = Backtrack(conjunto, self.numCaminhoes)
                    bactrack.resolver()
                    melhor_distribuicao_backtrack = bactrack.obter_melhor_distribuicao()
                    imprimir_distribuicao = bactrack.imprimir_melhor_distribuicao()
                fim = time.time()  # Tempo final de execução
                tempo_conjunto = (fim - inicio_execucao)  # Calcula o tempo de execução do conjunto
                self.tempoDeExecucaoBacktracking.append(tempo_conjunto)  # Adiciona em lista os tempos
                mediaTempo = sum(self.tempoDeExecucaoBacktracking) / len(self.tempoDeExecucaoBacktracking) # Calcula média
                quantRotas += 1  # Incrementa a quantidade de rotas


        except TimeoutError as te:
            print(te)

        finally:
            signal.alarm(0)  # Reset do temporizador após a conclusão ou exceção

        return mediaTempo, quantRotas


    def execucaoGulosoEstrategia1(self,quantRotas):
        quantRotasBacktracking = quantRotas
        totalRotasExecucao = quantRotas * 10
        while quantRotas <= totalRotasExecucao:
            conjunto_teste = GeradorDeProblemas.geracao_de_rotas(quantRotas, self.tamanho_conjunto, self.dispersao)
            inicio_execucao = time.time()
            for conjunto in conjunto_teste:
                estrategia1 = Greedy(self.numCaminhoes, conjunto)
                estrategia1.distribuir_rotas_menor()
                estrategia1.exibir_distribuicao('menor')
            fim = time.time()  # Tempo final de execução de cada tamanho
            tempo_conjunto = (fim - inicio_execucao)  # Calcula o tempo de execução do conjunto
            self.tempoDeExecucaoGulosoEstrategia1.append(tempo_conjunto)  # Adiciona em lista de tempos
            mediaTempo = sum(self.tempoDeExecucaoGulosoEstrategia1) / len(self.tempoDeExecucaoGulosoEstrategia1) # Calcula média
            quantRotas+=quantRotasBacktracking # Soma quantidade de rotas de acordo com Backtracking. Ex : 191, 382, 573

        return mediaTempo, totalRotasExecucao



    def execucaoGulosoEstrategia2(self,quantRotas):
        quantRotasBacktracking = quantRotas
        totalRotasExecusao = quantRotas * 10
        while quantRotas <= totalRotasExecusao:
            conjunto_teste = GeradorDeProblemas.geracao_de_rotas(quantRotas, self.tamanho_conjunto, self.dispersao)
            inicio_execucao = time.time()
            for conjunto in conjunto_teste:
                estrategia2 = Greedy(self.numCaminhoes, conjunto)
                estrategia2.distribuir_rotas_agrupamento()
                estrategia2.exibir_distribuicao('agrupamento')
            fim = time.time()  # Tempo final de execução
            tempo_conjunto = (fim - inicio_execucao)  # Calcula o tempo de execução do conjunto
            self.tempoDeExecucaoGulosoEstrategia2.append(tempo_conjunto)  # Adiciona em lista os tempos
            mediaTempo = sum(self.tempoDeExecucaoGulosoEstrategia2) / len(self.tempoDeExecucaoGulosoEstrategia2)
            print(quantRotas)
            quantRotas += quantRotasBacktracking # Soma quantidade de rotas de acordo com Backtracking. Ex : 191, 382, 573

        return mediaTempo, totalRotasExecusao


    def execucaoDivisaoConquista(self,quantRotasBacktracking):
        quantRotas = 6
        while quantRotas <= quantRotasBacktracking:
            conjunto_teste = GeradorDeProblemas.geracao_de_rotas(quantRotas, self.tamanho_conjunto, self.dispersao)
            inicio_execucao = time.time()
            for conjunto in conjunto_teste:
                print('------------------------')
                print('Conjunto em execução :')
                print(conjunto)
                divisaoConquista = MergeSort(conjunto, self.numCaminhoes)
                divisaoConquista.distribuir_quilometragem()
                divisaoConquista.imprimir_distribuicao()
            fim = time.time()  # Tempo final de execução de cada tamanho
            tempo_conjunto = (fim - inicio_execucao)  # Calcula o tempo de execução do conjunto
            self.tempoDeExecucaoDivisaoConquista.append(tempo_conjunto)  # Adiciona em lista os tempos
            mediaTempo = sum(self.tempoDeExecucaoDivisaoConquista)/len(self.tempoDeExecucaoDivisaoConquista)
            quantRotas+=1
        return mediaTempo, quantRotas

    def execucaoProgramacaoDinamica(self, quantRotas):
        totalRotasExecucao = quantRotas * 10
        while quantRotas <= totalRotasExecucao:
            conjunto_teste = GeradorDeProblemas.geracao_de_rotas(quantRotas, self.tamanho_conjunto, self.dispersao)
            inicio_execucao = time.time()
            for conjunto in conjunto_teste:
                distribuir_rotas(conjunto,self.numCaminhoes)
            fim = time.time()  # Tempo final de execução de cada tamanho
            tempo_conjunto = (fim - inicio_execucao)  # Calcula o tempo de execução do conjunto
            self.tempoDeExecucaoProgamacaoDinamica.append(tempo_conjunto)  # Adiciona em lista os tempos
            mediaTempo = sum(self.tempoDeExecucaoProgamacaoDinamica) / len(self.tempoDeExecucaoProgamacaoDinamica) # Calcula média
            quantRotas += 191
        return mediaTempo, quantRotas




if __name__ == "__main__":
    execucao = ExecucaoAlgoritmos()
    mediaTempoBacktacking, quantRotasBacktracking = execucao.execucaoBacktracking()
    print('Média de execução Backtracking : ', mediaTempoBacktacking)
    print('Quantidade de rotas Backtracking :', quantRotasBacktracking)

    '''mediaTempoGulosoEstrategia1, quantRotasGulosoEstrategia1 = execucao.execucaoGulosoEstrategia1(quantRotasBacktracking)
    print('Média de execução Guloso Estratégia 1 : ', mediaTempoGulosoEstrategia1)
    print('Quantidade de rotas Guloso Estratégia 1 :', quantRotasGulosoEstrategia1)

    mediaTempoGulosoEstrategia2, quantRotasGulosoEstrategia2 = execucao.execucaoGulosoEstrategia2(quantRotasBacktracking)
    print('Média de execução Guloso Estratégia 2 : ', mediaTempoGulosoEstrategia2)
    print('Quantidade de rotas Guloso Estratégia 2 :', quantRotasGulosoEstrategia2)

    mediaTempoDivisaoConquista, quantRotasDivisaoConquista = execucao.execucaoDivisaoConquista(quantRotasBacktracking)
    print('Média de execução Divisião por Conquista : ', mediaTempoDivisaoConquista)
    print('Quantidade de rotas Divisão por Conquista :', quantRotasDivisaoConquista)'''

    mediaTempoProgramacaoDinamica, quantRotasProgramacaoDinamica = execucao.execucaoProgramacaoDinamica(quantRotasBacktracking)
    print('Média de execução Programação Dinâmica : ', mediaTempoProgramacaoDinamica)
    print('Quantidade de rotas Programação Dinâmica :', quantRotasProgramacaoDinamica)

