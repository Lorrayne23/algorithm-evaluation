class Backtrack:
    def __init__(self, rotas, num_caminhoes):
        """ Classe é incializada  com rotas e o número de  caminhões. melhor_solucao e
        melhor_diferenca são variáveis que armazenarão a solução ótima e a menor
        diferença entre as quilometragens dos caminhões."""
        self.rotas = rotas
        self.num_caminhoes = num_caminhoes
        self.melhor_solucao = None
        self.melhor_diferenca = float("inf")

    def resolver(self):
        def backtrack(sol_parcial, idx_rota):
            # Verifica se é uma solução completa
            """  Verifica se todas as rotas foram
            distribuídas.Isso acontece quando
            o índice idx_rota é igual ao comprimento
            total de self.rotas"""

            if idx_rota == len(self.rotas):
                # Avalia a solução e atualiza a melhor solução se necessário
                """ Calcula a quilometragem total para cada caminhão em sol_parcial e, em seguida,
                 calcula a diferença entre a maior e a menor quilometragem entre todos os caminhões."""

                quilometragens = [sum(cam) for cam in sol_parcial]
                diferenca = max(quilometragens) - min(quilometragens)

                """ Verifica se a diferença  calculada é menor do que a melhor diferença já encontrada(self.melhor_diferenca).
                Se for , atualiza a melhor diferença e  a melhor solução encontrada até o momento.
                A melhor solução é uma cópia profunda (cam.copy()) da solução parcial atual."""

                if diferenca < self.melhor_diferenca:
                    self.melhor_diferenca = diferenca
                    self.melhor_solucao = [cam.copy() for cam in sol_parcial]
                return

            # Poda: Se a solução parcial atual não for promissora
            """Antes de realizar a exploração recursiva,
             o código verifica se a solução parcial atual não é promissora usando a função self.poda. 
             Se a solução não for promissora, o método backtrack retorna imediatamente,
              interrompendo a exploração desnecessária."""
            if not self.poda(sol_parcial, idx_rota):
                return

            # Exploração recursiva das decisões possíveis
            """Se a solução parcial for promissora, o código entra em um loop que percorre cada caminhão (i) disponível.
                Para cada caminhão, a rota atual (self.rotas[idx_rota]) é adicionada à solução parcial correspondente.
              E m seguida, a função backtrack é chamada recursivamente para explorar as decisões seguintes (idx_rota + 1).
           Após a chamada recursiva, a última decisão é desfeita para voltar ao estado anterior, garantindo que o algoritmo explore todas as possíveis combinações de decisões."""
            for i in range(self.num_caminhoes):
                sol_parcial[i].append(self.rotas[idx_rota])
                backtrack(sol_parcial, idx_rota + 1)
                sol_parcial[i].pop()  # Desfaz a decisão

        # Inicializa as soluções parciais
        solucao_parcial = [[] for _ in range(self.num_caminhoes)]

        # Inicia o backtracking
        backtrack(solucao_parcial, 0)

    def poda(self, sol_parcial, idx_rota):
        # Verifica se a solução parcial atual é promissora
        """ O método poda avalia a solução parcial atual calculando as quilometragens para cada caminhão e verificando se
        a diferença entre a maior e a menor quilometragem é menor ou igual à melhor diferença já encontrada.
         Se for o caso, a solução parcial é considerada promissora e a exploração recursiva continuará; caso contrário,
          a poda é aplicada e o ramo correspondente é podado (não explorado)"""
        quilometragens_atual = [sum(cam) for cam in sol_parcial]
        diferenca_atual = max(quilometragens_atual) - min(quilometragens_atual)
        return diferenca_atual <= self.melhor_diferenca

    # Retorna melhor solução
    def obter_melhor_distribuicao(self):
        return self.melhor_solucao

    # Imprime melhor distribuição para cada caminhaão
    def imprimir_melhor_distribuicao(self):
        for i, caminhao in enumerate(self.melhor_solucao, start=1):
            total_kms = sum(caminhao)
            rotas_formatadas = ", ".join([f"rota {rota}" for rota in caminhao])
            print(f"Caminhão {i}: {rotas_formatadas} – Total {total_kms}km")
