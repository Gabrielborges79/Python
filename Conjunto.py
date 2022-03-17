conjunto = {1,2,3,4,5}
conjunto2= {5,6,7,8}
conjunto3= conjunto.union(conjunto2)
print(conjunto3)
conjunto_interseccao=conjunto.intersection(conjunto2)
print(conjunto_interseccao)
conjunto_diferenca=conjunto.difference(conjunto2)
print(conjunto_diferenca)
conjunto_diferenca2=conjunto2.difference(conjunto)

conjunto_subset =conjunto2.issubset(conjunto)
print(conjunto_subset)

# print(type(conjunto))
# conjunto.add(5)
# conjunto.discard(2)
# print(conjunto)