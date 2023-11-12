import random

class GeradorDeProblemas:
    aleatorio = random.Random(42)
    TAM_BASE = 13

    @staticmethod
    def geracao_de_rotas(quant_rotas, tam_conjunto, dispersao):
        conjunto_de_teste = []
        tam_max = int(GeradorDeProblemas.TAM_BASE * (1 + dispersao))

        for _ in range(tam_conjunto):
            rotas = [GeradorDeProblemas.aleatorio.randint(GeradorDeProblemas.TAM_BASE, tam_max) for _ in range(quant_rotas)]
            conjunto_de_teste.append(rotas)

        return conjunto_de_teste



if __name__ == "__main__":
    # Exemplo de teste
    quant_rotas = 5
    tam_conjunto = 3
    dispersao = 0.5

    conjunto_de_teste = GeradorDeProblemas.geracao_de_rotas(quant_rotas, tam_conjunto, dispersao)
    print(conjunto_de_teste)

    # Imprime os conjuntos gerados
    for conjunto in conjunto_de_teste:
        print(conjunto)