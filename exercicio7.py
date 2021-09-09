filmes = ["forrest gump","fight club"]
jogos = ["mario","minecraft"]
livros = ["O senhor dos aneis","game of thrones"]
Esportes = ["basquete","futebol"]

#A
filmes.insert(1,"piratas do caribe") 
filmes.insert(2,"velozes e furiosos") 

jogos.insert(1,"sonic") 
jogos.insert(2,"cs") 

livros.insert(1,"the witcher") 
livros.insert(2,"Diario de um banana") 

Esportes.insert(1,"skate") 
Esportes.insert(2,"volei")

#B
lista = filmes + jogos + livros + Esportes

#C
print(livros[1])
#D
del Esportes[0]
lista = filmes + jogos + livros + Esportes

#E
disciplinas = ["geografia", "historia"]
lista = lista + disciplinas
print(lista)



