carro1: dict = {
    "nome": 'Golf GTI',
    "Potencia": 220,
    "Manco": "false"
}

carro2: dict = {
    "nome": 'Jetta GLI',
    "Potencia": 230,
    "Manco": "false"
}

carro3: dict = {
    "nome": 'Lancer CVT',
    "Potencia": 150,
    "Manco": "true"
}

carros = []

lista_carros = [carro1,carro2,carro3]

carros.extend(lista_carros)

print(carros)