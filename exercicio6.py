lista = ["lucas","joao","thiago","elias","nicolas","giordano","gabriel","augusto"]
nome = input("qual nome voce quer saber a posição que esta na lista?: ")
if nome in lista:
    print("Esta na posição: ",lista.index(nome))
else:
    print("Não tem como ver qual posição estao pois nao esta na lista")
