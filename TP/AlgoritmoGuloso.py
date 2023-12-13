class Greedy:
    def __init__(self, caminhoes, rotas):
        self.caminhoes = caminhoes
        self.rotas = rotas
        self.distribuicao_rotas_menor = [[] for _ in range(caminhoes)]
        self.quilometragem_caminhoes_menor = [0] * caminhoes
        self.distribuicao_rotas_agrupamento = [[] for _ in range(caminhoes)]
        self.quilometragem_caminhoes_agrupamento = [0] * caminhoes

    def distribuir_rotas_menor_quilometragem(self):
        for index, rota in enumerate(self.rotas):
            # Encontra o caminhão atual com a menor quilometragem acumulada
            caminhao_atual = min(range(self.caminhoes), key=lambda i: self.quilometragem_caminhoes_menor[i])

            # Atualiza a quilometragem do caminhão atual com a quilometragem da rota
            self.quilometragem_caminhoes_menor[caminhao_atual] += rota

            # Adiciona a rota ao caminhão atual na distribuição de rotas
            self.distribuicao_rotas_menor[caminhao_atual].append((index, rota))


    def distribuir_rotas_sequencial(self):
        # Estratégia: Atribuir as maiores rotas de forma sequencial aos três caminhões.

        # Ordena as rotas em ordem decrescente de quilometragem
        rotas_ordenadas = sorted(enumerate(self.rotas), key=lambda x: x[1], reverse=True)

        # Itera pelas rotas e atribui sequencialmente aos três caminhões
        for index, rota in rotas_ordenadas:
            # Obtém o próximo caminhão disponível (sequencialmente)
            caminhao_atual = index % self.caminhoes

            # Atualiza a quilometragem do caminhão atual com a quilometragem da rota
            self.quilometragem_caminhoes_agrupamento[caminhao_atual] += rota

            # Adiciona a rota ao caminhão atual na distribuição de rotas
            self.distribuicao_rotas_agrupamento[caminhao_atual].append((index,rota))

    def exibir_distribuicao(self, modo):
        distribuicao = getattr(self, f'distribuicao_rotas_{modo}')
        quilometragem_caminhoes = getattr(self, f'quilometragem_caminhoes_{modo}')
        for i, caminhao in enumerate(distribuicao):
            rotas = [rota[1] for rota in caminhao]
            total_quilometragem = sum(rotas)
            print(f"Caminhão {i + 1}: rotas {rotas} - total {total_quilometragem}km")




