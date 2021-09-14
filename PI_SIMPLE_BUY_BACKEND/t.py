# criando um estado
itemOf = ItemOf(nome='Parana')
BoItemOf = BoItemOf()
BoItemOf.create(itemOf)



# Selecionando todos os estados
itens_ = BoItemOf.selectAll(ItemOf)

print(ordens_de_fornecimentos)
