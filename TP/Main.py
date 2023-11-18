import time
import signal
from Backtracking import  Backtrack
from GeradorDeProblemas import GeradorDeProblemas
from AlgoritmoGuloso import Greedy
from DivisaoConquista import MergeSort

class ExecucaoAlgoritmos:
    def __init__(self):
        self.tempoDeExecucaoConjuntoBacktracking = []
        self.tempoDeExecucaoAlgoritmoGulosoEstrategia1 = []
        self.tempoDeExecucaoAlgoritmoGulosoEstrategia2 = []
        self.tempoDeExecucaoAlgoritmoDivisaoConquista = []
        self.numCaminhoes = 3
        self.tamanho_conjunto = 10
        self.dispersao = 0.7
        self.tempo_maximo = 30


    def execusaoGulosoEstrategia1(self,quantRotas):
        totalRotasExecusao = quantRotas * 10

        while quantRotas <= totalRotasExecusao:
            conjunto_teste = GeradorDeProblemas.geracao_de_rotas(quantRotas, self.tamanho_conjunto, self.dispersao)
            inicio_execucao = time.time()  # Tempo de início para calcular o tempo de execução
            for conjunto in conjunto_teste:
                estrategia1 = Greedy(self.numCaminhoes, conjunto)
                estrategia1.distribuir_rotas_menor()
                estrategia1.exibir_distribuicao('menor')
            fim = time.time()  # Tempo final de execução de cada tamanho
            tempo_conjunto = (fim - inicio_execucao)  # Calcula o tempo de execução do conjunto
            self.tempoDeExecucaoAlgoritmoGulosoEstrategia1.append(tempo_conjunto)  # Adiciona em lista os tempos de cada tamanho
            mediaTempo = sum(self.tempoDeExecucaoAlgoritmoGulosoEstrategia1) / len(self.tempoDeExecucaoAlgoritmoGulosoEstrategia1)
            quantRotas+=1

        return mediaTempo, totalRotasExecusao



    def execusaoGulosoEstrategia2(self,quantRotas):
        totalRotasExecusao = quantRotas * 10
        inicio_execucao = time.time()  # Tempo de início para calcular o tempo de
        while quantRotas <= totalRotasExecusao:
            conjunto_teste = GeradorDeProblemas.geracao_de_rotas(quantRotas, self.tamanho_conjunto, self.dispersao)
            inicio_execucao = time.time()  # Tempo de início para calcular o tempo de execução
            for conjunto in conjunto_teste:
                estrategia2 = Greedy(self.numCaminhoes, conjunto)
                estrategia2.distribuir_rotas_agrupamento()
                estrategia2.exibir_distribuicao('agrupamento')
            fim = time.time()  # Tempo final de execução de cada tamanho
            tempo_conjunto = (fim - inicio_execucao)  # Calcula o tempo de execução do conjunto
            self.tempoDeExecucaoAlgoritmoGulosoEstrategia2.append(tempo_conjunto)  # Adiciona em lista os tempos de cada tamanho
            mediaTempo = sum(self.tempoDeExecucaoAlgoritmoGulosoEstrategia2) / len(
                self.tempoDeExecucaoAlgoritmoGulosoEstrategia2)
            quantRotas += 1

        return mediaTempo, totalRotasExecusao


    def execusaoDivisaoConquista(self,quantRotasBacktracking):
        quantRotas = 6
        while quantRotas != quantRotasBacktracking:
            conjunto_teste = GeradorDeProblemas.geracao_de_rotas(quantRotas, self.tamanho_conjunto, self.dispersao)
            inicio_execucao = time.time()  # Tempo de início para calcular o tempo de execução
            for conjunto in conjunto_teste:
                print('------------------------')
                print('Conjunto em execução :')
                print(conjunto)
                divisaoConquista = MergeSort(conjunto, self.numCaminhoes)
                divisaoConquista.distribuir_quilometragem()
                divisaoConquista.imprimir_distribuicao()
            fim = time.time()  # Tempo final de execução de cada tamanho
            tempo_conjunto = (fim - inicio_execucao)  # Calcula o tempo de execução do conjunto
            self.tempoDeExecucaoAlgoritmoDivisaoConquista.append(tempo_conjunto)  # Adiciona em lista os tempos de cada tamanho
            mediaTempo = sum(self.tempoDeExecucaoAlgoritmoDivisaoConquista)/len(self.tempoDeExecucaoAlgoritmoDivisaoConquista)
            quantRotas+=1
            print(quantRotas)
        return mediaTempo, quantRotas

    def execusaoBacktracking(self):
        def handler(signum, frame):
            raise TimeoutError("Tempo máximo de execução atingido")

        signal.signal(signal.SIGALRM, handler)
        signal.alarm(self.tempo_maximo)

        try:
            quantRotas = 6
            while True:
                conjunto_teste = GeradorDeProblemas.geracao_de_rotas(quantRotas, self.tamanho_conjunto, self.dispersao)
                inicio_execucao = time.time()  # Tempo de início para calcular o tempo de execução
                for conjunto in conjunto_teste:
                    bactrack = Backtrack(conjunto, self.numCaminhoes)
                    bactrack.resolver()
                    melhor_distribuicao_backtrack = bactrack.obter_melhor_distribuicao()
                fim = time.time()  # Tempo final de execução
                tempo_conjunto = (fim - inicio_execucao)  # Calcula o tempo de execução do conjunto
                self.tempoDeExecucaoConjuntoBacktracking.append(
                    tempo_conjunto)  # Adiciona em lista os tempos de cada tamanho
                mediaTempo = sum(self.tempoDeExecucaoConjuntoBacktracking) / len(self.tempoDeExecucaoConjuntoBacktracking)
                quantRotas += 1  # Incrementa a quantidade de rotas


        except TimeoutError as te:
            print(te)

        finally:
            signal.alarm(0)  # Reset do temporizador após a conclusão ou exceção

        return mediaTempo, quantRotas

if __name__ == "__main__":
    execucao = ExecucaoAlgoritmos()
    mediaTempoBacktacking, quantRotasBacktracking = execucao.execusaoBacktracking()
    print('Média de execução Backtracking : ', mediaTempoBacktacking)
    print('Quantidade de rotas Backtracking :', quantRotasBacktracking)

    mediaTempoGulosoEstrategia1, quantRotaGulosoEstrategia1 = execucao.execusaoGulosoEstrategia1(quantRotasBacktracking)
    print('Média de execução Guloso Estratégia 1 : ', mediaTempoGulosoEstrategia1)
    print('Quantidade de rotas Guloso Estratégia 1 :', quantRotaGulosoEstrategia1)

    mediaTempoGulosoEstrategia2, quantRotasGulosoEstrategia2 = execucao.execusaoGulosoEstrategia2(quantRotasBacktracking)
    print('Média de execução Guloso Estratégia 2 : ', mediaTempoGulosoEstrategia2)
    print('Quantidade de rotas Guloso Estratégia 2 :', quantRotasGulosoEstrategia2)

    mediaTempoDivisaoConquista, quantRotasDivisaoConquista = execucao.execusaoDivisaoConquista(quantRotasBacktracking)
    print('Média de execução Guloso Estratégia 2 : ', mediaTempoDivisaoConquista)
    print('Quantidade de rotas Guloso Estratégia 2 :', quantRotasDivisaoConquista)


