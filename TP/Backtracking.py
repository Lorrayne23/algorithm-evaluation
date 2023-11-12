class Backtracking:
    def __init__(self, rotas, num_caminhoes):
        self.rotas = rotas
        self.num_caminhoes = num_caminhoes
        self.melhor_solucao = None
        self.melhor_diferenca = float('inf')

    def resolver(self):
        def backtrack(sol_parcial, idx_rota):
            # Verifica se é uma solução completa
            if idx_rota == len(self.rotas):
                # Avalia a solução e atualiza a melhor solução se necessário
                quilometragens = [sum(cam) for cam in sol_parcial]
                diferenca = max(quilometragens) - min(quilometragens)

                if diferenca < self.melhor_diferenca:
                    self.melhor_diferenca = diferenca
                    self.melhor_solucao = [cam.copy() for cam in sol_parcial]
                return

            # Exploração recursiva das decisões possíveis
            for i in range(self.num_caminhoes):
                sol_parcial[i].append(self.rotas[idx_rota])
                backtrack(sol_parcial, idx_rota + 1)
                sol_parcial[i].pop()  # Desfaz a decisão

        # Inicializa as soluções parciais
        solucao_parcial = [[] for _ in range(self.num_caminhoes)]

        # Inicia o backtracking
        backtrack(solucao_parcial, 0)

    def obter_melhor_distribuicao(self):
        return self.melhor_solucao

    def imprimir_melhor_distribuicao(self):
        for i, caminhao in enumerate(self.melhor_solucao, start=1):
            total_kms = sum(caminhao)
            rotas_formatadas = ", ".join([f"rota {rota}" for rota in caminhao])
            print(f"Caminhão {i}: {rotas_formatadas} – Total {total_kms}km")

# Exemplo de uso
rotas_exemplo = [35, 34, 33, 23, 21, 32, 35, 19, 26, 42]
num_caminhoes_exemplo = 3

distribuicao = Backtracking(rotas_exemplo, num_caminhoes_exemplo)
distribuicao.resolver()
melhor_distribuicao = distribuicao.obter_melhor_distribuicao()
distribuicao.imprimir_melhor_distribuicao()

print("Melhor distribuição:", melhor_distribuicao)
