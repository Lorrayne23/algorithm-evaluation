class Greedy:
    def __init__(self, caminhoes, rotas):
        self.caminhoes = caminhoes
        self.rotas = rotas
        self.distribuicao_rotas_menor = [[] for _ in range(caminhoes)]
        self.quilometragem_caminhoes_menor = [0] * caminhoes
        self.distribuicao_rotas_agrupamento = [[] for _ in range(caminhoes)]
        self.quilometragem_caminhoes_agrupamento = [0] * caminhoes

    def distribuir_rotas_menor(self):
        # Estratégia: Aloca cada rota ao caminhão com a menor quilometragem acumulada até o momento.
        # Ordena as rotas em ordem decrescente de quilometragem
        rotas_ordenadas = sorted(enumerate(self.rotas), key=lambda x: x[1], reverse=True)
        for index, rota in rotas_ordenadas:
            # Encontra o caminhão atual com a menor quilometragem acumulada
            caminhao_atual = min(range(self.caminhoes), key=lambda i: self.quilometragem_caminhoes_menor[i])
            # Atualiza a quilometragem do caminhão atual com a quilometragem da rota
            self.quilometragem_caminhoes_menor[caminhao_atual] += rota
            # Adiciona a rota ao caminhão atual na distribuição de rotas
            self.distribuicao_rotas_menor[caminhao_atual].append((index, rota))

    def distribuir_rotas_agrupamento(self):
        # Estratégia: Prioriza rotas próximas fisicamente para minimizar a quilometragem total percorrida.
        # As rotas são ordenadas por quilometragem, e cada rota é atribuída ao caminhão que minimiza a alteração na quilometragem acumulada,
        # considerando também o número de rotas já atribuídas.

        # Ordena as rotas em ordem decrescente de quilometragem, mantendo os índices originais
        rotas_ordenadas = sorted(enumerate(self.rotas), key=lambda x: x[1], reverse=True)
        for index, rota in rotas_ordenadas:
            # Obtém a lista de caminhões disponíveis e a ordena com base em uma chave composta
            caminhoes_disponiveis = list(range(self.caminhoes))
            caminhoes_disponiveis = list(range(self.caminhoes))
            caminhoes_disponiveis.sort(key=lambda i: (
                abs(self.quilometragem_caminhoes_agrupamento[i] + rota - sum(
                    x[1] for x in self.distribuicao_rotas_agrupamento[i])),
                len(self.distribuicao_rotas_agrupamento[i])
            ))
            # Escolhe o caminhão atual como o primeiro da lista ordenada de caminhões disponíveis
            caminhao_atual = caminhoes_disponiveis[0]

            # Atualiza a quilometragem do caminhão atual com a quilometragem da rota
            self.quilometragem_caminhoes_agrupamento[caminhao_atual] += rota

            # Adiciona a rota ao caminhão atual na distribuição de rotas
            self.distribuicao_rotas_agrupamento[caminhao_atual].append((index, rota))

    def exibir_distribuicao(self, modo):
        distribuicao = getattr(self, f'distribuicao_rotas_{modo}')
        quilometragem_caminhoes = getattr(self, f'quilometragem_caminhoes_{modo}')
        for i, caminhao in enumerate(distribuicao):
            rotas = [rota[1] for rota in caminhao]
            total_quilometragem = sum(rotas)
            print(f"Caminhão {i + 1}: rotas {rotas} - total {total_quilometragem}km")




