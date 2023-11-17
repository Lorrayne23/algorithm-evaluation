import time
import signal
from Backtracking import  Backtrack
from GeradorDeProblemas import GeradorDeProblemas
from AlgoritmoGuloso import Greedy

class ExecucaoAlgoritmos:
    def __init__(self):
        self.tempoDeExecucaoConjuntoBacktracking = []
        self.tempoDeExecucaoAlgoritmoGulosoEstrategia1 = []
        self.tempoDeExecucaoAlgoritmoGulosoEstrategia2 = []
        self.numCaminhoes = 3
        self.tamanho_conjunto = 10
        self.dispersao = 0.7
        self.tempo_maximo = 30

    def backtrack(self,conjunto_teste):
        inicio_execucao = time.time()  # Tempo de início para calcular o tempo de execução
        for conjunto in conjunto_teste:
            print('------------------------')
            print('Conjunto em execução :')
            print(conjunto)

            bactrack = Backtrack(conjunto, self.numCaminhoes)
            bactrack.resolver()
            melhor_distribuicao_backtrack = bactrack.obter_melhor_distribuicao()
            bactrack.imprimir_melhor_distribuicao()
            print(melhor_distribuicao_backtrack)
        fim = time.time()  # Tempo final de execução de cada tamanho
        tempo_conjunto = (fim - inicio_execucao)  # Calcula o tempo de execução do conjunto
        self.tempoDeExecucaoConjuntoBacktracking.append(tempo_conjunto)  # Adiciona em lista os tempos de cada tamanho

    def gulosoEstrategia1(self,conjunto_teste):
        inicio_execucao = time.time()  # Tempo de início para calcular o tempo de execução
        for conjunto in conjunto_teste:
            print('------------------------')
            print('Conjunto em execução :')
            print(conjunto)
            estrategia1 = Greedy(self.numCaminhoes, conjunto)
            estrategia1.distribuir_rotas_menor()
            estrategia1.exibir_distribuicao('menor')
        fim = time.time()  # Tempo final de execução de cada tamanho
        tempo_conjunto = (fim - inicio_execucao)  # Calcula o tempo de execução do conjunto
        self.tempoDeExecucaoAlgoritmoGulosoEstrategia1.append(tempo_conjunto)  # Adiciona em lista os tempos de cada tamanho


    def gulosoEstrategia2(self,conjunto_teste):
        inicio_execucao = time.time()  # Tempo de início para calcular o tempo de execução
        for conjunto in conjunto_teste:
            print('------------------------')
            print('Conjunto em execução :')
            print(conjunto)
            estrategia2 = Greedy(self.numCaminhoes, conjunto)
            estrategia2.distribuir_rotas_agrupamento()
            estrategia2.exibir_distribuicao('agrupamento')
        fim = time.time()  # Tempo final de execução de cada tamanho
        tempo_conjunto = (fim - inicio_execucao)  # Calcula o tempo de execução do conjunto
        self.tempoDeExecucaoAlgoritmoGulosoEstrategia2.append(tempo_conjunto)  # Adiciona em lista os tempos de cada tamanho

    def executar_backtracking(self):
        def handler(signum, frame):
            raise TimeoutError("Tempo máximo de execução atingido")

        signal.signal(signal.SIGALRM, handler)
        signal.alarm(self.tempo_maximo)

        try:
            quant_rotas = 6
            while True:
                print('-------------------')
                print('Quantidade de rotas :', quant_rotas)
                conjunto_teste = GeradorDeProblemas.geracao_de_rotas(quant_rotas, self.tamanho_conjunto,self.dispersao)
                print('-----------------------')
                print('Conjunto de teste gerado:')
                print(conjunto_teste)
                self.backtrack(conjunto_teste)
                self.gulosoEstrategia1(conjunto_teste)
                self.gulosoEstrategia2(conjunto_teste)
                quant_rotas += 1  # Incrementa a quantidade de rotas

        except TimeoutError as te:
            print(te)

        finally:
            signal.alarm(0)  # Reset do temporizador após a conclusão ou exceção

if __name__ == "__main__":
    execucao = ExecucaoAlgoritmos()
    execucao.executar_backtracking()
