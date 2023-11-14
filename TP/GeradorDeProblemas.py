import random

class GeradorDeProblemas:
    aleatorio = random.Random(42)
    TAM_BASE = 13


    def geracao_de_rotas(quant_rotas, tam_conjunto, dispersao):
        conjunto_de_teste = []
        tam_max = int(GeradorDeProblemas.TAM_BASE * (1 + dispersao))

        for _ in range(tam_conjunto):
            rotas = [GeradorDeProblemas.aleatorio.randint(GeradorDeProblemas.TAM_BASE, tam_max) for _ in range(quant_rotas)]
            conjunto_de_teste.append(rotas)

        return conjunto_de_teste



