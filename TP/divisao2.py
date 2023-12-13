class DistribuicaoRotas:
    def __init__(self, rotas, num_caminhoes):
        self.rotas = rotas
        self.num_caminhoes = num_caminhoes
        self.distribuicao = [[] for _ in range(num_caminhoes)]
        self.total_quilometragem = [0] * num_caminhoes

    def divisao_e_conquista(self, caminhoes, rotas):
        if len(rotas) == 0:
            return

        if len(rotas) == 1:
            caminhao_idx = self.total_quilometragem.index(min(self.total_quilometragem))
            self.distribuicao[caminhao_idx].append(rotas[0])
            self.total_quilometragem[caminhao_idx] += rotas[0]
            return

        rotas.sort(reverse=True)

        meio = len(rotas) // 2
        self.divisao_e_conquista(caminhoes, rotas[:meio])
        self.divisao_e_conquista(caminhoes, rotas[meio:])

    def distribuir_quilometragem(self):
        self.divisao_e_conquista(self.num_caminhoes, self.rotas)

    def imprimir_distribuicao(self):
        for i, caminhao_rotas in enumerate(self.distribuicao):
            print(f'Caminhão {i + 1}: rotas {caminhao_rotas} - total {self.total_quilometragem[i]}km')


