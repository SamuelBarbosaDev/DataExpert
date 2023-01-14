import numpy as np
import matplotlib.pyplot as plt

usuario = {
    'Hugo Araújo': {
        'nome': 'Hugo Araújo',
        'idade': 28,
        'salario': 15000,
    },
    'Laissa Padilha': {
        'nome': 'Laissa Padilha',
        'idade': 31,
        'salario': 10000,
    },
    'Murilo Cechin': {
        'nome': 'Murilo Cechin',
        'idade': 24,
        'salario': 10000,
    },
    'Agostinho José': {
        'nome': 'Agostinho José',
        'idade': 22,
        'salario': 14000,
    },
    'Filipe Tavares': {
        'nome': 'Filipe Tavares',
        'idade': 32,
        'salario': 15000,
    },
    'Moisés Nascimento': {
        'nome': 'Moisés Nascimento',
        'idade': 32,
        'salario': 20000,
    },
    'Pedro Beghelli': {
        'nome': 'Pedro Beghelli',
        'idade': 27,
        'salario': 15000,
    },
    'Alexandre Kuroda': {
        'nome': 'Alexandre Kuroda',
        'idade': 33,
        'salario': 25000,
    }
}

media_lista = [
    15000,
    10000,
    10000,
    14000,
    15000,
    20000,
    15000,
    25000
]

media = sum(media_lista) / len(media_lista)

for index, value in enumerate(usuario):
    print(f"""
    nome: {usuario[value]['nome']}
    salario: {usuario[value]['salario']}
    idade: {usuario[value]['idade']}
    """)

print(f'a media é: {media}')

plt.figure(figsize=(100, 200))
plt.title('meu título')
