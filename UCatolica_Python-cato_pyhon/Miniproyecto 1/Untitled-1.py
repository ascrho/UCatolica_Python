csv1 = open("C:\\Users\\marco\\OneDrive\\Escritorio\\Otros Cursos\\U Catolica\\Cursos\\Python - Desarrollo de Software\\CLASE 2\Miniproyecto 1\\peliculas.csv","r")
list1 = list(csv1)
csv1.close()

generos_peliculas=list()

for i in range(len(list1)):
    if i > 0:
        list2 = list1[i].split(",")
        list3 = list2[4].split(";")
        for i in range(len(list3)):
            generos_peliculas.append(list3[i].replace("\n","")) if list3[i].replace("\n","") not in generos_peliculas else generos_peliculas

peliculas_por_genero = list()
listaTupla1 = list()
peli_x_gen = list()
peli_x_gen2 = tuple()

for i in range(len(list1)):
    if i > 0:
        list2 = list1[i].split(",")
        list3 = list2[4].split(";")
        peli1 = list2[0]
        for i in range(len(list3)):
            gene1 = list3[i].replace("\n","")
            t = [(gene1,[peli1])]
            listaTupla1 = listaTupla1 + t

for i in range(len(generos_peliculas)):
    
    gene2 = generos_peliculas[i]
    print(gene2)
    for i in range(len(listaTupla1)):
        if gene2 == listaTupla1[i][0]:
            peli2 = listaTupla1[i][1]
            peli_x_gen = peli_x_gen + peli2
            peli_x_gen2 = tuple([gene2]+[peli_x_gen])
peliculas_por_genero.append(peli_x_gen2)

print(peliculas_por_genero)