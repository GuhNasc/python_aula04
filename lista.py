# Exemplos de lista

# Carros para ser inserido na lista
carro1: str = "Golf GTI"
carro2: str = "Passat B8"
carro3: str = "Jetta GLI"

# Criando uma lista vazia
carros: list = []

# Adicionando carros na lista vazia usando APPEND
carros.append(carro1)
carros.append(carro2)
carros.append(carro3)

# Removendo o ultimo carro da lista
carros.pop()

# Adicionando mais 5 carros de uma vez usando o extend

carro4: str ='La Ferrari'
carro5: str = 'Pagani'

novos_carros = [carro4, carro5]

carros.extend(novos_carros)

#Printando a lista
print(carros)