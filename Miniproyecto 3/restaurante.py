##############################################################

## Si necesita agregar imports, debe agregarlos aquí arriba ##


### INICIO PARTE 3 ###
class Restaurante:
    def __init__(self, nombre, platos, cocineros, repartidores):
        self.nombre = str(nombre)
        self.platos = platos # Es un diccionario que posee todos los platos del restaurante, donde cada llave es el nombre de un plato y su valor es una lista con el nombre del plato y su tipo.
        self.cocineros = cocineros # Es una lista con los cocineros del restaurante, los cuales son instancias de la clase Cocinero.
        self.repartidores = repartidores # Es una lista con los repartidores del restaurante, los cuales son instancias de la clase Repartidor.
        self.calificacion = 0

    def recibir_pedidos(self, clientes):
    # clientes es una lista de objetos de la clase Cliente(platos_preferidos)
    # platos_preferidos: Es una lista con los nombres de los platos preferidos del cliente. Se recibe como parámetro de inicialización (pueden ser entre 1 y 5 nombres de platos).        

    # cocineros: Es una lista con los cocineros del restaurante, los cuales son instancias de la clase Cocinero. Se recibe como parámetro de inicialización.
    # Cocinero, atributo energia inicializado, metodo cocinar(informacion_plato), informacion_plato, es una lista con el nombre y el tipo del plato a cocinar, donde el tipo puede ser "Bebestible" o "Comestible"
        
    #pedido, es una lista de objetos de la clase Bebestible o Comestible

    #Repartidor, posee el metodo repartir(pedido) que recibe como argumento una lista de platos.

        #Lista de clientes
        for cl in range(len(clientes)):
            self.pedido = []
            self.demora = 0
            #lista de platos del cliente
            #La variable plato, toma uno a uno los nombres de los platos
            for pf in range(len(clientes[cl].platos_preferidos)):
                plato = self.platos[clientes[cl].platos_preferidos[pf]]

                #Lista de cocineros
                for co in range(len(self.cocineros)):
                    if self.cocineros[co].energia > 0:
                        self.pedido.append(self.cocineros[co].cocinar(plato)) # Va agregando los platos a medida que se van preparando, siempre que algun cocinero tenga energia
                        break
            #else:
            #    print(f"{str(clientes[cl].nombre)[2:-2]} ordeno {len(clientes[cl].platos_preferidos)} platos, se prepararon {len(self.pedido)}.") #Permite conocer la cantidad de platos que fueron preparados

        # Una vez los platos de la lista de este cliente fueron cocinados o no, y fueran agregados a la lista pedido, se entregan a algun repartidor con energia
            for rp in range(len(self.repartidores)):
                if self.repartidores[rp].energia > 0:
                    self.repartidores[rp].repartir(self.pedido)
                    self.demora = self.repartidores[rp].tiempo_entrega
                    #print(f"{str(clientes[cl].nombre)[2:-2]} recibio {len(self.pedido)} platos de su pedido, se demoraron {self.demora} segundos en entregarlo.") #Permite conocer la cantidad de platos que fueron preparados
                    break

            if self.demora == 0:
                self.pedido = []
                self.demora = 0

            clientes[cl].recibir_pedido(self.pedido,self.demora)
            self.calificacion += clientes[cl].calificacion
            print(f"{str(clientes[cl].nombre)[2:-2]} ordeno {len(clientes[cl].platos_preferidos)} platos y recibio {len(self.pedido)} platos en su pedido, se demoraron {self.demora} segundos en entregarlo y califico con {clientes[cl].calificacion}.") #Permite conocer la cantidad de platos que fueron preparados

        self.calificacion = (self.calificacion/len(clientes))
        #print(f"La calificación final es de {self.calificacion}") Permite conocer la calificación final

### FIN PARTE 3 #


if __name__ == "__main__":

    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        PLATOS_PRUEBA = {
        "Pepsi": ["Pepsi", "Bebestible"],
        "Mariscos": ["Mariscos", "Comestible"],
        }
        un_restaurante = Restaurante("Bon Appetit", PLATOS_PRUEBA, [], [])
        print(f"El restaurante {un_restaurante.nombre}, tiene los siguientes platos:")
        for plato in un_restaurante.platos.values():
            print(f" - {plato[1]}: {plato[0]}")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")
