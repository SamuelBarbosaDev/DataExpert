import numpy as np


class EstudoNumpy():
    def __init__(self):
        """
        Criando as matrizes.
        """
        self.matriz_array = np.array(
            [[1, 2, 3], [9, 8, 7]]
        )
        self.matriz_arange = np.arange(3, 11)
        self.matriz_linspace = np.linspace(5, 25, num=5)

    def retorna_informações_das_matrizes(self):
        tamanho_da_matriz_array = self.matriz_array.shape
        quantidades_de_linhas_array = self.matriz_array.ndim

        tamanho_da_matriz_arange = self.matriz_arange.shape
        quantidades_de_linhas_arange = self.matriz_arange.ndim

        print(f"""
        --array--
        o tamanho da array em cada dimensão: {tamanho_da_matriz_array}|
        Quantidade de linhas: {quantidades_de_linhas_array}|

        --arange--
        o tamanho da array em cada dimensão: {tamanho_da_matriz_arange}|
        Quantidade de linhas: {quantidades_de_linhas_arange}|

        --linspace--
        printando a matriz_linspace: {self.matriz_linspace}|
        """)


if __name__ == '__main__':
    estudo_numpy = EstudoNumpy()
    estudo_numpy.retorna_informações_das_matrizes()
