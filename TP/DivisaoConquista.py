class MergeSort:
    def __init__(self, rotas, num_caminhoes):
        self.rotas = rotas
        self.num_caminhoes = num_caminhoes
        self.distribuicao = [[] for _ in range(num_caminhoes)]
        self.total_quilometragem = [0] * num_caminhoes

    def merge_sort(self, arr):
        """
               Implementa o algoritmo de ordenação merge sort.

               Parâmetros:
               - arr: Lista a ser ordenada.
               """
        if len(arr) > 1:
            meio = len(arr) // 2
            metade_esquerda = arr[:meio]
            metade_direita = arr[meio:]

            # Chamadas recursivas para ordenar as metades.
            self.merge_sort(metade_esquerda)
            self.merge_sort(metade_direita)

            i = j = k = 0
            # Combina as metades ordenadas em uma única lista ordenada.
            while i < len(metade_esquerda) and j < len(metade_direita):
                if metade_esquerda[i] < metade_direita[j]:
                    arr[k] = metade_esquerda[i]
                    i += 1
                else:
                    arr[k] = metade_direita[j]
                    j += 1
                k += 1
            # Adiciona elementos restantes, se houver.
            while i < len(metade_esquerda):
                arr[k] = metade_esquerda[i]
                i += 1
                k += 1

            while j < len(metade_direita):
                arr[k] = metade_direita[j]
                j += 1
                k += 1

    def distribuir_quilometragem(self):
        """
                Distribui as rotas entre os caminhões após ordenar as rotas usando merge sort.
                """
        # Chama o método merge_sort para ordenar a lista de rotas.
        self.merge_sort(self.rotas)
        for rota in self.rotas:
            # Encontra o caminhão com a menor quilometragem total e atribui a rota a esse caminhão.
            caminhao_idx = self.total_quilometragem.index(min(self.total_quilometragem))
            self.distribuicao[caminhao_idx].append(rota)
            self.total_quilometragem[caminhao_idx] += rota

    def imprimir_distribuicao(self):
        """
             Imprime a distribuição de rotas entre os caminhões.
        """
        for i, caminhao_rotas in enumerate(self.distribuicao):
            print(f'Caminhão {i + 1}: rotas {caminhao_rotas} - total {self.total_quilometragem[i]}km')


# Exemplo de uso
'''rotas = [35, 34, 33, 23, 21, 32, 35, 19, 26, 42]
num_caminhoes = 5

distribuicao_caminhoes = MergeSort(rotas, num_caminhoes)
distribuicao_caminhoes.distribuir_quilometragem()
distribuicao_caminhoes.imprimir_distribuicao()'''
