#comando input(): quero permitir que
#o usuário digete algo...
nome = input("Digite seu nome: ")

idade = int(input("Digite sua idade: "))
#comando de saída..exibir na tela
print(nome)
print(f"Boa noite, seu nome é {nome}")
#exiba "Sua idade é "
print("Sua idade é {}".format(idade))


#e se eu quissesse mostra o Dobro da idade informada
dobro = idade *2
print("O dobro da idade informada é {}".format(dobro))
