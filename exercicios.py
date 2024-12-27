# 1 Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. 
# Imprima cada informação.

#from typing import Dict, Any
#
#livro: dict[str, any] = {
#    "Nome":"Harry Potter",
#    "Autor": "J. K. Rowling",
#    "Ano": 2005 
#}
#
#livro2: dict[str, any] = {
#    "Nome":"Harry Potter - 2",
#    "Autor": "J. K. Rowling",
#    "Ano": 2007 
#}
#
#livro3: dict[str, any] = {
#    "Nome":"Harry Potter - 3",
#    "Autor": "J. K. Rowling",
#    "Ano": 2009
#}
#
#hp: list = [livro, livro2, livro3]
#
#for idx, livro in enumerate(hp, start=1):
#    print(f"Livro {idx}:")
#    for chave, valor in livro.items():
#        print(f"  {chave}: {valor}")
#    print()  


# 2 Crie um programa que armazene informações de 5 alunos em uma lista. Cada aluno deve ser representado por um dicionário contendo nome, idade e nota. 
# Depois, percorra a lista e mostre as informações de cada aluno no seguinte formato:
#Aluno 1:
#  Nome: João
#  Idade: 20
#  Nota: 8.5


####################################################### O QUE DESENVOLVI ####################################################################
#
## Lista para armazenar os alunos
#lista_alunos: list = []
#
## Loop para adicionar múltiplos alunos
#while True:
#    # Coletando dados do aluno
#    nome: str = input("Digite seu nome: ").strip()
#    idade: int = int(input("Digite sua idade: "))
#    nota: float = float(input("Digite sua nota: "))
#
#    # Validação do nome
#    if not nome.replace(" ", "").isalpha():
#        print("Nome INVÁLIDO. O nome deve conter apenas letras e espaços.")
#        continue  # Reinicia o loop para pedir os dados novamente
#
#    # Validação da idade
#    if not (18 <= idade <= 70):
#        print("Idade fora do range permitido (18 a 70 anos).")
#        continue
#
#    # Validação da nota
#    if nota < 0 or nota > 10:
#        print("Nota inválida. Digite uma nota entre 0 e 10.")
#        continue
#
#    # Exibindo o resultado da validação da nota
#    if nota > 5:
#        print(f"{nome}, você passou na matéria!")
#    else:
#        print(f"{nome}, você reprovou.")
#
#    # Criando o dicionário do aluno
#    aluno: dict = {
#        'Nome': nome,
#        'Idade': idade,
#        'Nota': nota
#    }
#
#    # Adicionando o aluno à lista
#    lista_alunos.append(aluno)
#
#    # Perguntar se deseja adicionar outro aluno
#    continuar = input("Deseja adicionar outro aluno? (s/n): ").strip().lower()
#    if continuar != 's':
#        break
#
## Exibindo a lista final de alunos
#print("\nLista de Alunos:")
#for idx, aluno in enumerate(lista_alunos, start=1):
#    print(f"Aluno {idx}:")
#    for chave, valor in aluno.items():
#        print(f"  {chave}: {valor}")
#    print()

###################
###################
###################

# 3  Contador de Frutas Crie uma lista contendo os nomes de frutas, onde algumas frutas aparecem repetidas. 
# Use um dicionário para contar quantas vezes cada fruta aparece na lista. No final, mostre a contagem de cada fruta.

#frutas = ["maçã", "banana", "maçã", "laranja", "banana", "uva"]
#
#dicionario_frutas: dict = {}
#
#for fruta in frutas:
#    if fruta in dicionario_frutas:
#        dicionario_frutas[fruta] += 1
#    else:
#        dicionario_frutas[fruta] = 1
#
#print (dicionario_frutas)


# 4 Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

#linguagens = ["Python", "Java", "C++", "JavaScript"]
#
#linguagens.pop(2)
#
#linguagens.append('Ruby')
#
#print(linguagens)

# 5 Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado

lista = list(range(1,11))
for numero in lista:
    print(numero **2)