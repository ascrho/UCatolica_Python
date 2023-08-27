##############################################################
from random import randint
from platos import Comestible, Bebestible
## Si necesita agregar imports, debe agregarlos aquí arriba ##


### INICIO PARTE 2.1 ###
class Persona:
    def __init__(self, nombre):
        self.nombre = str(nombre)
    
### FIN PARTE 2.1 ###

### INICIO PARTE 2.2 ###
class Repartidor(Persona):
    def __init__(self, nombre, tiempo_entrega):
        super().__init__(nombre)
        self.tiempo_entrega = tiempo_entrega
        self.energia = randint(75,100)
    
    def repartir(self, pedido):
        self.factor_tamaño = 0
        self.factor_velocidad = 0

        if len(pedido) <= 2:
            self.factor_tamaño = 5
            self.energia -= self.factor_tamaño
        elif len(pedido) >= 3:
            self.factor_tamaño = 15
            self.energia -= self.factor_tamaño

        if len(pedido) <= 2:
            self.factor_velocidad = 1.25
            self.tiempo_entrega = self.tiempo_entrega * self.factor_velocidad
        elif len(pedido) >= 3:
            self.factor_velocidad = 0.85
            self.tiempo_entrega = self.tiempo_entrega * self.factor_velocidad
        
        return self.tiempo_entrega

### FIN PARTE 2.2 ###

### INICIO PARTE 2.3 ###
class Cocinero(Persona):
    def __init__(self, nombre, habilidad):
        super().__init__(nombre)
        self.habilidad = habilidad
        self.energia = randint(50,80)
    
    def cocinar(self, informacion_plato):
        self.plato = "Plato"
        self.factor_calidad = 0

        if informacion_plato[1] == "Bebestible":
            self.plato = Bebestible(informacion_plato[0])
            if self.plato.tamano == "Pequeño":
                self.energia -= 5
            elif self.plato.tamano == "Mediano":
                self.energia -= 8
            elif self.plato.tamano == "Grande":
                self.energia -= 10

        elif informacion_plato[1] == "Comestible":
            self.plato = Comestible(informacion_plato[0])
            self.energia -= 15

        if self.plato.dificultad > self.habilidad:
            self.factor_calidad = 0.7
            self.plato.calidad = self.plato.calidad * self.factor_calidad
        else:
            self.factor_calidad = 1.5
            self.plato.calidad = self.plato.calidad * self.factor_calidad
        
        return(self.plato)
        
### FIN PARTE 2.3 ###

### INICIO PARTE 2.4 ###
class Cliente(Persona):
    def __init__(self, nombre, platos_preferidos):
        super().__init__(nombre)
        self.platos_preferidos = platos_preferidos

    def recibir_pedido(self, pedido, demora):

        self.calificacion = 10

        if len(pedido) < len(self.platos_preferidos) or demora >= 20:
            self.calificacion = self.calificacion / 2
        
        for i in range(len(pedido)):
            if pedido[i].calidad >= 11:
                self.calificacion += 1.5
            elif pedido[i].calidad <= 8:
                self.calificacion -= 3
        
        return self.calificacion

### FIN PARTE 2.4 ###

if __name__ == "__main__":

    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        PLATOS_PRUEBA = {
        "Jugo Natural": ["Jugo Natural", "Bebestible"],
        "Empanadas": ["Empanadas", "Comestible"],
        }
        un_cocinero = Cocinero("Cristian", randint(1, 10))
        un_repartidor = Repartidor("Tomás", randint(20, 30))
        un_cliente = Cliente("Alberto", PLATOS_PRUEBA)
        print(f"El cocinero {un_cocinero.nombre} tiene una habilidad: {un_cocinero.habilidad}")
        print(f"El repatidor {un_repartidor.nombre} tiene una tiempo de entrega: {un_repartidor.tiempo_entrega} seg")
        print(f"El cliente {un_cliente.nombre} tiene los siguientes platos favoritos:")
        for plato in un_cliente.platos_preferidos.values():
            print(f" - {plato[1]}: {plato[0]}")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")
