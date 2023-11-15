class DistribuicaoRotas:
    def __init__(self, caminhoes, rotas):
        self.caminhoes = caminhoes
        self.rotas = rotas
        self.distribuicao_rotas_menor = [[] for _ in range(caminhoes)]
        self.quilometragem_caminhoes_menor = [0] * caminhoes
        self.distribuicao_rotas_maior = [[] for _ in range(caminhoes)]
        self.quilometragem_caminhoes_maior = [0] * caminhoes

    def distribuir_rotas_menor(self):
        rotas_ordenadas = sorted(enumerate(self.rotas), key=lambda x: x[1], reverse=True)
        for index, rota in rotas_ordenadas:
            caminhao_atual = min(range(self.caminhoes), key=lambda i: self.quilometragem_caminhoes_menor[i])
            self.quilometragem_caminhoes_menor[caminhao_atual] += rota
            self.distribuicao_rotas_menor[caminhao_atual].append((index, rota))

    def distribuir_rotas_maior(self):
        rotas_ordenadas = sorted(enumerate(self.rotas), key=lambda x: x[1])
        # Aloca cada rota ao caminhão com a menor quilometragem acumulada até o momento
        for index, rota in rotas_ordenadas:
            caminhao_atual = min(range(self.caminhoes), key=lambda i: self.quilometragem_caminhoes_maior[i])
            self.quilometragem_caminhoes_maior[caminhao_atual] += rota
            self.distribuicao_rotas_maior[caminhao_atual].append((index, rota))

    def exibir_distribuicao(self, modo):
        distribuicao = getattr(self, f'distribuicao_rotas_{modo}')
        quilometragem_caminhoes = getattr(self, f'quilometragem_caminhoes_{modo}')

        for i, caminhao in enumerate(distribuicao):
            rotas = [rota[1] for rota in caminhao]
            total_quilometragem = sum(rotas)
            print(f"Caminhão {i + 1}: rotas {rotas} - total {total_quilometragem}km")

# Exemplo de uso
caminhoes = 4
rotas = [35, 34, 33, 23, 21, 32, 35, 19, 26, 42]

# Cria uma nova instância da classe e realiza a distribuição usando a estratégia de menor quilometragem primeiro
distribuicao_menor = DistribuicaoRotas(caminhoes, rotas)
distribuicao_menor.distribuir_rotas_menor()

# Exibe o resultado da distribuição usando a estratégia de menor quilometragem primeiro
print("Distribuição usando a estratégia de menor quilometragem primeiro:")
distribuicao_menor.exibir_distribuicao('menor')

# Cria uma nova instância da classe e realiza a distribuição usando a estratégia de maior quilometragem primeiro
distribuicao_maior = DistribuicaoRotas(caminhoes, rotas)
distribuicao_maior.distribuir_rotas_maior()

# Exibe o resultado da distribuição usando a estratégia de maior quilometragem primeiro
print("\nDistribuição usando a estratégia de maior quilometragem primeiro:")
distribuicao_maior.exibir_distribuicao('maior')
