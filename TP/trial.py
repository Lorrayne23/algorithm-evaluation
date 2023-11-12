def backtracking(rotas, num_caminhoes):
    melhor_solucao = None
    melhor_diferenca = float('inf')

    def backtrack(sol_parcial, idx_rota):
        nonlocal melhor_solucao, melhor_diferenca

        # Verifica se é uma solução completa
        if idx_rota == len(rotas):
            # Avalia a solução e atualiza a melhor solução se necessário
            quilometragens = [sum(cam) for cam in sol_parcial]
            diferenca = max(quilometragens) - min(quilometragens)

            if diferenca < melhor_diferenca:
                melhor_diferenca = diferenca
                melhor_solucao = [cam.copy() for cam in sol_parcial]
            return

        # Exploração recursiva das decisões possíveis
        for i in range(num_caminhoes):
            sol_parcial[i].append(rotas[idx_rota])
            backtrack(sol_parcial, idx_rota + 1)
            sol_parcial[i].pop()  # Desfaz a decisão

    # Inicializa as soluções parciais
    solucao_parcial = [[] for _ in range(num_caminhoes)]

    # Inicia o backtracking
    backtrack(solucao_parcial, 0)

    return melhor_solucao

# Exemplo de uso
rotas_exemplo = [35, 34, 33, 23, 21, 32, 35, 19, 26, 42]
num_caminhoes_exemplo = 4
melhor_distribuicao = backtracking(rotas_exemplo, num_caminhoes_exemplo)
print("Melhor distribuição:", melhor_distribuicao)
