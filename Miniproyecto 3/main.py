##############################################################
from random import seed, randint, sample
import personas as prs
import restaurante as rest
## Si necesita agregar imports, debe agregarlos aquí arriba ##


### INICIO PARTE 4 ###

def crear_repartidores():
    repartidores = []
    for i in range(2):
        nombre = sample(list(NOMBRES),1)
        tiempo_entrega = randint(20,30)
        repartidor1 = prs.Repartidor(nombre,tiempo_entrega)
        repartidores.append(repartidor1)
    return repartidores

def crear_cocineros():

    cocineros = []
    for i in range(5):
        habilidad = randint(1,10)
        nombre = sample(list(NOMBRES),1)
        cocinero = prs.Cocinero(nombre,habilidad)
        cocineros.append(cocinero)

    return cocineros

def crear_clientes():
    
    clientes = []
    for i in range(5):
        cant_platos = randint(1,5)
        platos = sample(list(INFO_PLATOS),cant_platos)
        nombre = sample(list(NOMBRES),1)
        cliente = prs.Cliente(nombre,platos)
        clientes.append(cliente)

    return clientes

def crear_restaurante():
    cocineros = crear_cocineros()
    repartidores = crear_repartidores()
    restaurante = rest.Restaurante("Tablas Del Saladillo",INFO_PLATOS,cocineros,repartidores)
    return restaurante

### FIN PARTE 4 ###

################################################################
## No debe modificar nada de abajo en este archivo.
## Este archivo debe ser ejecutado para probar el funcionamiento
## de su programa orientado a objetos.
################################################################

INFO_PLATOS = {
    "Pepsi": ["Pepsi", "Bebestible"],
    "Coca-Cola": ["Coca-Cola", "Bebestible"],
    "Jugo Natural": ["Jugo Natural", "Bebestible"],
    "Agua": ["Agua", "Bebestible"],
    "Papas Duqueza": ["Papas Duqueza", "Comestible"],
    "Lomo a lo Pobre": ["Lomo a lo Pobre", "Comestible"],
    "Empanadas": ["Empanadas", "Comestible"],
    "Mariscos": ["Mariscos", "Comestible"],
}

NOMBRES = ["Cristian", "Antonio", "Francisca", "Camila", "Caua"]

if __name__ == "__main__":

    ### Código para probar que tu miniproyecto esté funcionando correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    seed("DSP")
    restaurante = crear_restaurante() # Crea el restaurante a partir de la función crear_restaurante()
    clientes = crear_clientes() # Crea los clientes a partir de la función crear_clientes()
    if restaurante != None and clientes != None:
        restaurante.recibir_pedidos(clientes) # Corre el método recibir_pedidos(clientes) para actualizar la calificación del restaurante
        print(
            f"La calificación final del restaurante {restaurante.nombre} "
            f"es {restaurante.calificacion}"
        )
    elif restaurante == None:
        print("la funcion crear_restaurante() no esta retornando la instancia del restaurante")
    elif clientes == None:
        print("la funcion crear_clientes() no esta retornando la instancia de los clientes")
