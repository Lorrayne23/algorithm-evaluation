def distribuir_rotas(rotas, num_caminhoes):
    m = len(rotas)

    # Inicializa a matriz de programação dinâmica
    dp = [[float('inf')] * (m + 1) for _ in range(num_caminhoes + 1)]
    dp[0][0] = 0

    # Calcula a diferença de quilometragem mínima para cada combinação de caminhão e rota
    for i in range(1, num_caminhoes + 1):
        for j in range(1, m + 1):
            dp[i][j] = min(dp[i][j-1], dp[i-1][j-1] + rotas[j-1])

    # Recupera a distribuição mínima de quilometragem
    distribuicao = [[] for _ in range(num_caminhoes)]
    i, j = num_caminhoes, m
    while j > 0:
        distribuicao[i-1].append(rotas[j-1])
        i = i - 1 if i > 1 else num_caminhoes  # Volta ao último caminhão se necessário
        j -= 1

    # Imprime a distribuição de quilometragem mínima
    for idx, caminhao in enumerate(distribuicao):
        total_kms = sum(caminhao)
        print(f'Caminhão {idx + 1}: rotas {", ".join(map(str, caminhao))} - total {total_kms}km')

# Execução local
'''num_caminhoes = 5
rotas = [35, 34, 33, 23, 21, 32, 35, 19, 26, 42]
distribuir_rotas(rotas, num_caminhoes)'''
