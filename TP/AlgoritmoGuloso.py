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
        rotas_ordenadas = sorted(enumerate(self.rotas), key=lambda x: x[1], reverse=True)
        for index, rota in rotas_ordenadas:
            caminhao_atual = min(range(self.caminhoes), key=lambda i: self.quilometragem_caminhoes_menor[i])
            self.quilometragem_caminhoes_menor[caminhao_atual] += rota
            self.distribuicao_rotas_menor[caminhao_atual].append((index, rota))

    def distribuir_rotas_agrupamento(self):
        # Estratégia: Priorizando rotas próximas fisicamente para minimizar a quilometragem total percorrida.
        # As rotas são ordenadas por quilometragem, e cada rota é atribuída ao caminhão que minimiza a alteração na quilometragem acumulada,
        # considerando também o número de rotas já atribuídas.
        rotas_ordenadas = sorted(enumerate(self.rotas), key=lambda x: x[1], reverse=True)
        for index, rota in rotas_ordenadas:
            caminhoes_disponiveis = list(range(self.caminhoes))
            caminhoes_disponiveis.sort(key=lambda i: (
                abs(self.quilometragem_caminhoes_agrupamento[i] + rota - sum(
                    x[1] for x in self.distribuicao_rotas_agrupamento[i])),
                len(self.distribuicao_rotas_agrupamento[i])
            ))

            caminhao_atual = caminhoes_disponiveis[0]
            self.quilometragem_caminhoes_agrupamento[caminhao_atual] += rota
            self.distribuicao_rotas_agrupamento[caminhao_atual].append((index, rota))

    def exibir_distribuicao(self, modo):
        distribuicao = getattr(self, f'distribuicao_rotas_{modo}')
        quilometragem_caminhoes = getattr(self, f'quilometragem_caminhoes_{modo}')
        for i, caminhao in enumerate(distribuicao):
            rotas = [rota[1] for rota in caminhao]
            total_quilometragem = sum(rotas)
            print(f"Caminhão {i + 1}: rotas {rotas} - total {total_quilometragem}km")


# Exemplo de uso
caminhoes = 3
rotas = [35, 34, 33, 23, 21, 32, 35, 19, 26, 42]

# Cria uma nova instância da classe e realiza a distribuição usando a estratégia de menor quilometragem primeiro
distribuicao_menor = Greedy(caminhoes, rotas)
distribuicao_menor.distribuir_rotas_menor()

# Exibe o resultado da distribuição usando a estratégia de menor quilometragem primeiro
print("Distribuição usando a estratégia de menor quilometragem primeiro:")
distribuicao_menor.exibir_distribuicao('menor')

# Cria uma nova instância da classe e realiza a distribuição usando a estratégia de agrupamento
distribuicao_agrupamento = Greedy(caminhoes, rotas)
distribuicao_agrupamento.distribuir_rotas_agrupamento()

# Exibe o resultado da distribuição usando a estratégia de agrupamento
print("\nDistribuição usando a estratégia de agrupamento:")
distribuicao_agrupamento.exibir_distribuicao('agrupamento')
