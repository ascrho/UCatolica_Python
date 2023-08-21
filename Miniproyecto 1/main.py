# Parte 1: Cargar los datos

def leer_archivo():
    lineas_archivo = []
    csv1 = open("C:\\Users\\marco\\OneDrive\\Escritorio\\Otros Cursos\\U Catolica\\Cursos\\Python - Desarrollo de Software\\CLASE 2\Miniproyecto 1\\peliculas.csv","r",encoding="utf-8")
    with csv1 as datos:
        for linea in datos.readlines()[1:]:
            lineas_archivo.append(linea.strip())
    csv1.close()
    return lineas_archivo

def cargar_datos(lineas_archivo):
    # Completar

    #########################################
    #generos_peliculas
    #########################################
    generos_peliculas=list()

    for i in range(len(lineas_archivo)):
        list2 = lineas_archivo[i].split(",")
        list3 = list2[4].split(";")
        for i in range(len(list3)):
            generos_peliculas.append(list3[i].replace("\n","")) if list3[i].replace("\n","") not in generos_peliculas else generos_peliculas
    #print(generos_peliculas)

    #########################################
    #peliculas_por_genero
    #########################################
    peliculas_por_genero = list()
    listaTupla1 = list()

    for i in range(len(lineas_archivo)):
        list2 = lineas_archivo[i].split(",")
        list3 = list2[4].split(";")
        peli1 = list2[0]
            
        #Elimina el caracter "\n"
        for i in range(len(list3)):
            gene1 = list3[i].replace("\n","")
            t = [(gene1,[peli1])]
            listaTupla1 = listaTupla1 + t

    for i in range(len(generos_peliculas)):
        gene2 = generos_peliculas[i]
        peli_x_gen = list()
        for i in range(len(listaTupla1)):
            if gene2 == listaTupla1[i][0]:
                peli2 = listaTupla1[i][1]
                peli_x_gen = peli_x_gen + peli2
        if bool(peliculas_por_genero):
            peliculas_por_genero = peliculas_por_genero + [tuple([gene2,peli_x_gen])]
        else:
            peliculas_por_genero = [tuple([gene2,peli_x_gen])]

    #########################################
    #info_peliculas
    #########################################
    info_peliculas = list()

    for i in range(len(lineas_archivo)):
        list2 = lineas_archivo[i].split(",")
        titulo1 = list2[0]
        popularidad1 = list2[1]
        vpromedio1 = list2[2]
        cvotos1 = list2[3]
        generos1 = list2[4].split(";")
            
        #Elimina el caracter "\n"
        generos2 = list()
        for i in range(len(generos1)):
            g2 = generos1[i].replace("\n","")
            if bool(g2):
                generos2 = generos2 + [g2]
            else:
                generos2 = g2

        t = [(titulo1,popularidad1,vpromedio1,cvotos1,generos2)]

        if bool(info_peliculas):
            info_peliculas = info_peliculas + t
        else:
            info_peliculas = t
    return generos_peliculas, peliculas_por_genero, info_peliculas #Esta estructura retorna una tupla


# Parte 2: Completar las consultas
def obtener_puntaje_y_votos(nombre_pelicula):
    # Cargar las lineas con la data del archivo
    lineas_archivo = leer_archivo()

    # Completar con lo que falta aquí
    info_peliculas = cargar_datos(lineas_archivo)[2]
    for i in range(len(info_peliculas)):
        if nombre_pelicula == info_peliculas[i][0]:
            ppromedio = info_peliculas[i][2]
            votos = info_peliculas[i][3]
    return ppromedio, votos


def filtrar_y_ordenar(genero_pelicula):
    # Cargar las lineas con la data del archivo
    lineas_archivo = leer_archivo()
    # Completar con lo que falta aquí
    peliculas_por_genero = cargar_datos(lineas_archivo)[1]
    for i in range(len(peliculas_por_genero)):
        if genero_pelicula == peliculas_por_genero[i][0]:
            peliculas = sorted(sorted(peliculas_por_genero[i][1]), key=sorted(peliculas_por_genero[i][1]).index, reverse=True)
    return peliculas

def obtener_estadisticas(genero_pelicula, criterio):
    # Cargar las lineas con la data del archivo
    lineas_archivo = leer_archivo()

    # Completar con lo que falta aquí
    info_peliculas = cargar_datos(lineas_archivo)[2]
    stapopu1l = []
    stavprom1l = []
    stacantvot1l = []

    for i in range(len(info_peliculas)):

        if genero_pelicula in info_peliculas[i][4]:

            stapopu1 = float(info_peliculas[i][1])
            stavprom1 = float(info_peliculas[i][2])
            stacantvot1 = int(info_peliculas[i][3])
            
            stapopu1l = stapopu1l + [stapopu1]
            stavprom1l = stavprom1l + [stavprom1]
            stacantvot1l = stacantvot1l + [stacantvot1]

    if criterio == "popularidad":
        minpop = sorted(stapopu1l)[0]
        maxpop = sorted(stapopu1l)[-1]
        propop = round(sum(stapopu1l)/len(stapopu1l),3)
        estadisticas = [maxpop,minpop,propop]
    elif criterio == "voto promedio":
        maxvot = sorted(stavprom1l)[0]
        minvot = sorted(stavprom1l)[-1]
        stavot = round(sum(stavprom1l)/len(stavprom1l),3)
        estadisticas = [maxvot,minvot,stavot]
    elif criterio == "cantidad votos":
        maxcan = sorted(stacantvot1l)[0]
        mincan = sorted(stacantvot1l)[-1]
        stacan = round(sum(stacantvot1l)/len(stacantvot1l),3)
        estadisticas = [maxcan,mincan,stacan]

    return estadisticas

# NO ES NECESARIO MODIFICAR DESDE AQUI HACIA ABAJO

def solicitar_accion():
    print("\n¿Qué desea hacer?\n")
    print("[0] Revisar estructuras de datos")
    print("[1] Obtener puntaje y votos de una película")
    print("[2] Filtrar y ordenar películas")
    print("[3] Obtener estadísticas de películas")
    print("[4] Salir")

    eleccion = input("\nIndique su elección (0, 1, 2, 3, 4): ")
    while eleccion not in "01234":
        eleccion = input("\nElección no válida.\nIndique su elección (0, 1, 2, 3, 4): ")
    eleccion = int(eleccion)
    return eleccion


def leer_archivo():
    lineas_peliculas = []
    with open("peliculas.csv", "r", encoding="utf-8") as datos:
        for linea in datos.readlines()[1:]:
            lineas_peliculas.append(linea.strip())
    return lineas_peliculas


def revisar_estructuras(generos_peliculas, peliculas_por_genero, info_peliculas):
    print("\nGéneros de películas:")
    for genero in generos_peliculas:
        print(f"    - {genero}")

    print("\nTítulos de películas por genero:")
    for genero in peliculas_por_genero:
        print(f"    genero: {genero[0]}")
        for titulo in genero[1]:
            print(f"        - {titulo}")

    print("\nInformación de cada película:")
    for pelicula in info_peliculas:
        print(f"    Nombre: {pelicula[0]}")
        print(f"        - Popularidad: {pelicula[1]}")
        print(f"        - Puntaje Promedio: {pelicula[2]}")
        print(f"        - Votos: {pelicula[3]}")
        print(f"        - Géneros: {pelicula[4]}")


def solicitar_nombre():
    nombre = input("\nIngrese el nombre de la película: ")
    return nombre


def solicitar_genero():
    genero = input("\nIndique el género de película: ")
    return genero


def solicitar_genero_y_criterio():
    genero = input("\nIndique el género de película: ")
    criterio = input(
        "\nIndique el criterio (popularidad, voto promedio, cantidad votos): "
    )
    return genero, criterio


def main():
    lineas_archivo = leer_archivo()
    datos_cargados = True
    try:
        generos_peliculas, peliculas_por_genero, info_peliculas = cargar_datos(
            lineas_archivo
        )
    except TypeError as error:
        if "cannot unpack non-iterable NoneType object" in repr(error):
            print(
                "\nTodavía no puedes ejecutar el programa ya que no has cargado los datos\n"
            )
            datos_cargados = False
    if datos_cargados:
        salir = False
        print("\n********** ¡Bienvenid@! **********")
        while not salir:
            accion = solicitar_accion()

            if accion == 0:
                revisar_estructuras(
                    generos_peliculas, peliculas_por_genero, info_peliculas
                )

            elif accion == 1:
                nombre_pelicula = solicitar_nombre()
                ptje, votos = obtener_puntaje_y_votos(nombre_pelicula)
                print(f"\nObteniendo puntaje promedio y votos de {nombre_pelicula}")
                print(f"    - Puntaje promedio: {ptje}")
                print(f"    - Votos: {votos}")

            elif accion == 2:
                genero = solicitar_genero()
                nombres_peliculas = filtrar_y_ordenar(genero)
                print(f"\nNombres de películas del género {genero} ordenados:")
                for nombre in nombres_peliculas:
                    print(f"    - {nombre}")

            elif accion == 3:
                genero, criterio = solicitar_genero_y_criterio()
                estadisticas = obtener_estadisticas(genero, criterio)
                print(f"\nEstadísticas de {criterio} de películas del género {genero}:")
                print(f"    - Máximo: {estadisticas[0]}")
                print(f"    - Mínimo: {estadisticas[1]}")
                print(f"    - Promedio: {estadisticas[2]}")

            else:
                salir = True
        print("\n********** ¡Adiós! **********\n")


if __name__ == "__main__":
    main()
