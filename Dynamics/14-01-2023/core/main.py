import matplotlib.pyplot as plt

usuario = {
    'Samuel Barbosa': {
        'nome': 'Samuel Barbosa',
        'idade': 19,
        'salario': 300000,
    },
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
nome = [
    'Samuel Barbosa',
    'Hugo Araújo',
    'Laissa Padilha',
    'Murilo Cechin',
    'Agostinho José',
    'Filipe Tavares',
    'Moisés Nascimento',
    'Pedro Beghelli',
    'Alexandre Kuroda',
]

idade = [
    19,
    28,
    31,
    24,
    22,
    32,
    32,
    27,
    33,
]

salario = [
    300000,
    15000,
    10000,
    10000,
    14000,
    15000,
    20000,
    15000,
    25000
]

media = sum(salario) / len(salario)

for index, value in enumerate(usuario):
    print(f"""
    nome: {usuario[value]['nome']}
    salario: {usuario[value]['salario']}
    idade: {usuario[value]['idade']}
    """)

print(f'a media é: {media}')

plt.figure(figsize=(100, 200))
plt.bar()
plt.show()
