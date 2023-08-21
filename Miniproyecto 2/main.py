import parametros as p
import random

# NO MODIFICAR
class Rueda:
    def __init__(self):
        self.resistencia_actual = random.randint(*p.RESISTENCIA)
        self.resistencia_total = self.resistencia_actual
        self.estado = "Perfecto"

    def gastar(self, accion, tipo):
        if accion == "acelerar":
            if tipo == "automovil":
                self.resistencia_actual -= 5
            elif tipo == "moto":
                self.resistencia_actual -= 3
        elif accion == "frenar":
            if tipo == "automovil":
                self.resistencia_actual -= 10
            elif tipo == "moto":
                self.resistencia_actual -= 7
        self.actualizar_estado()

    def actualizar_estado(self):
        if self.resistencia_actual < 0:
            self.estado = "Rota"
        elif self.resistencia_actual < self.resistencia_total / 2:
            self.estado = "Gastada"
        elif self.resistencia_actual < self.resistencia_total:
            self.estado = "Usada"


# NO MODIFICAR

def seleccionar(vehiculos):
    if not len(vehiculos):
        print("No hay vehículos instanciados todavía")
        return

    print("Los vehículos disponibles son:")
    for indice in range(len(vehiculos)):
        print(f"[{indice}] {str(vehiculos[indice])}")

    elegido = int(input())
    while elegido < 0 or elegido >= len(vehiculos):
        print("intentelo de nuevo.")
        elegido = int(input())

    vehiculo = vehiculos[elegido]
    print("Se seleccionó el vehículo", str(vehiculo))
    return vehiculo


# Parte 1: Definición de clases

def avanzar(velocidad, tiempo):
    float(velocidad) #mt/seg
    int(tiempo) #seg

    kilometraje = velocidad*tiempo #mt/seg*seg
    return kilometraje #m

class Automovil():

    def __init__(self, kilometraje, ano):
        self.kilometraje = kilometraje #Km
        self.ano = ano
        self.ruedas = []
        for i in range(4):
            rueda=Rueda()
            self.ruedas.append(rueda)
        self.aceleracion = 0 #Km/Hr2
        self.velocidad = 0 #Km/Hr

    def avanzar(self,tiempo):
        int(tiempo)#seg
        VelocidadMS = (self.velocidad*1000)/3600 #Km/Hr -> mt/seg
        self.kilometraje += (avanzar(tiempo,VelocidadMS))/1000 #mt -> Km

    def acelerar(self,tiempo):
        int(tiempo) #Hr
        self.aceleracion += tiempo*0.5 #K/Hr2 Incrementa la aceleracion del atributo de instancia aceleracion
        self.velocidad += self.aceleracion * tiempo * 3.6 #Km/Hr
        tiempo = (tiempo*3600) #Hr -> seg
        self.avanzar(tiempo) #Setea velocidad(mt/seg) e incrementa kilometraje(Km)
        #Ejecuta el metodo gastar a cada rueda
        for i in range(4):
            self.ruedas[i].gastar("acelerar","automovil")
        self.aceleracion = 0

    def frenar(self,tiempo):
        int(tiempo) #Hr
        self.aceleracion -= tiempo*0.5 #Km/Hr2 Reduce la aceleracion del atributo de instancia aceleracion
        self.velocidad += self.aceleracion * tiempo * 3.6 #Km/Hr
        #Si velocidad es negativa, entonces igualar a 0
        if (self.velocidad < 0):
            self.velocidad = 0
        #Convierte el tiempo ingresado en Hr en seg
        tiempo = (tiempo*3600) #Hr -> seg
        self.avanzar(tiempo) #Setea velocidad(mt/seg) e incrementa kilometraje(Km)
        #Ejecuta el metodo gastar a cada rueda
        for i in range(4):
            self.ruedas[i].gastar("frenar","automovil")
        self.aceleracion = 0

    def obtener_kilometraje(self):
        return self.kilometraje

    def reemplazar_rueda(self):
        #Crea una lista vacia
        resitencia = []
        #Inserta en la lista los valores de resitencia de cada una de las reudas
        for i in range(len(self.ruedas)):
            resitencia.append(self.ruedas[i].resistencia_actual)
        #Encuentra el valor de resistencia mas bajo, y retorna su indice
        rueda_gastada = resitencia.index(min(resitencia))
        #Elimina el indice determinado en el paso anterior
        del self.ruedas[rueda_gastada]
        #Crea un objeto rueda_repuesto de la clase Rueda
        rueda_repuesto=Rueda()
        #Inserta rueda_repuesto dentro de ruedas
        self.ruedas.insert(rueda_gastada,rueda_repuesto)
        
    def __str__(self):
        return f"Automóvil del año {self.ano}"

class Moto():

    def __init__(self, kilometraje, ano, cilindrada):
        self.kilometraje = kilometraje #Km
        self.ano = ano
        self.ruedas = []
        for i in range(2):
            rueda=Rueda()
            self.ruedas.append(rueda)
        self.aceleracion = 0 #Km/h2
        self.velocidad = 0 #Km/h
        #Se usa el metodo val_neg, para evitar que se ingresen valores negativos
        self.cilindrada = self.val_neg(int(cilindrada))

    #Este metodo retorna el error definido en raise, si el valor que recibe es menor a 0
    def val_neg(self,cilindrada):
        if cilindrada < 0:
            raise ValueError("Cilindrada debe ser un valor mayor o igual a 0.")
        return cilindrada

    def avanzar(self,tiempo):
        int(tiempo)#seg
        VelocidadMS = (self.velocidad*1000)/3600 #Km/Hr -> mt/seg
        self.kilometraje += (avanzar(tiempo,VelocidadMS))/1000 #Km

    def acelerar(self,tiempo):
        int(tiempo) #Hr
        self.aceleracion += (tiempo*0.8) + (self.cilindrada*0.2) #Km/Hr2 Incrementa la aceleracion del atributo de instancia aceleracion
        self.velocidad += self.aceleracion * tiempo * 3 #Km/Hr
        #Convierte el tiempo ingresado en Hr en seg
        tiempo = (tiempo*3600) #Hr -> seg
        self.avanzar(tiempo) #Setea velocidad(mt/seg) e incrementa kilometraje(Km)
        #Ejecuta el metodo gastar a cada rueda
        for i in range(2):
            self.ruedas[i].gastar("acelerar","moto")
        self.aceleracion = 0

    def frenar(self,tiempo):
        int(tiempo) #seg
        tiempo = (tiempo/3600) #seg -> Hr
        self.aceleracion -= (tiempo*0.8) + (self.cilindrada*0.2) # Km/Hr2 Reduce la aceleracion del atributo de instancia aceleracion
        self.velocidad += self.aceleracion * tiempo * 3 #Km/Hr
        #Si velocidad es negativa, entonces igualar a 0
        if (self.velocidad < 0):
            self.velocidad = 0
        tiempo = (tiempo*3600) #Hr -> seg
        self.avanzar(tiempo) #Setea velocidad(mt/seg) e incrementa kilometraje(Km)
        #Ejecuta el metodo gastar a cada rueda
        for i in range(2):
            self.ruedas[i].gastar("frenar","moto")
        self.aceleracion = 0

    def obtener_kilometraje(self):
        return self.kilometraje

    def reemplazar_rueda(self):
        #Recorre las ruedas existentes
        for i in range(len(self.ruedas)):
            #Si alguna rueda tiene una resistencia actual menor a la mitad de la resistencia total
            if self.ruedas[i].resistencia_actual < self.ruedas[i].resistencia_total/2:
                #Encuentra la rueda y retorna su indice
                rueda_gastada = self.ruedas.index(self.ruedas[i])
                #Elimina de la lista el indice determinado en el paso anterior
                del self.ruedas[rueda_gastada]
                #Crea un objeto rueda_repuesto de la clase Rueda
                rueda_repuesto=Rueda()
                #Inserta rueda_repuesto dentro de ruedas
                self.ruedas.insert(rueda_gastada,rueda_repuesto)

    def __str__(self):
        return f"Moto del año {self.ano}."

# Parte 2: Completar acciones

def accion(vehiculo, opcion):
    # Completar
    if opcion == 2:  # Acelerar
        if "Automovil" in str(type(vehiculo)):
            tiempo = float(input("Indique el tiempo en Horas para acelerar el vehiculo:"))
            vehiculo.acelerar(tiempo)
            print(f"Se ha acelerado por {tiempo} horas, llegando a una velocidad de {vehiculo.velocidad} km/h.")
        elif "Moto" in str(type(vehiculo)):
            tiempo = float(input("Indique el tiempo en Horas para acelerar el vehiculo:"))
            vehiculo.acelerar(tiempo)
            print(f"Se ha acelerado por {tiempo} horas, llegando a una velocidad de {vehiculo.velocidad} km/h.")
        else:
            print("Vehiculo no encontrado. Intente nuevamente.")

    elif opcion == 3:  # Frenar
        if "Automovil" in str(type(vehiculo)):
            tiempo_frenar = float(input("Indique el tiempo en Horas para frenar el vehiculo:"))
            vehiculo.frenar(tiempo_frenar)
            print(f"Se ha frenado por {tiempo_frenar} horas, llegando a una velocidad de {vehiculo.velocidad} km/h.")
        elif "Moto" in str(type(vehiculo)):
            tiempo_frenar = float(input("Indique el tiempo en Segundos para frenar el vehiculo:"))
            vehiculo.frenar(tiempo_frenar)
            print(f"Se ha frenado por {tiempo_frenar} Segundos, llegando a una velocidad de {vehiculo.velocidad} km/h.")
        else:
            print("Vehiculo no encontrado. Intente nuevamente.")

    elif opcion == 4:  # Avanzar
        if "Automovil" in str(type(vehiculo)):
            tiempo_avanzar = float(input("Indique el tiempo en Segundos para frenar el vehiculo:"))
            vehiculo.avanzar(tiempo_avanzar)
            print(f"Se ha avanzado por {tiempo_avanzar} segundos, llegando a una velocidad de {vehiculo.velocidad} km/h y con un kilometraje de {vehiculo.kilometraje} Km.")
        elif "Moto" in str(type(vehiculo)):
            tiempo_avanzar = float(input("Indique el tiempo en Segundos para frenar el vehiculo:"))
            vehiculo.avanzar(tiempo_avanzar)
            print(f"Se ha avanzado por {tiempo_avanzar} segundos, llegando a una velocidad de {vehiculo.velocidad} km/h y con un kilometraje de {vehiculo.kilometraje} Km.")
        else:
            print("Vehiculo no encontrado. Intente nuevamente.")

    elif opcion == 5:  # Cambiar rueda
        if "Automovil" in str(type(vehiculo)):
            vehiculo.reemplazar_rueda()
            print(f"Se han reemplazado las ruedas con éxito")
        elif "Moto" in str(type(vehiculo)):
            vehiculo.reemplazar_rueda()
            print("Se han reemplazado las ruedas con éxito")
        else:
            print("Vehiculo no encontrado. Intente nuevamente.")

    elif opcion == 6:  # Mostrar Estado
        if "Automovil" in str(type(vehiculo)):
            print(f"El año del vehiculo es {vehiculo.ano}, se encuentra actualmente desplazandose a una velocidad de {vehiculo.velocidad} km/h con un kilometraje de {vehiculo.obtener_kilometraje()} Km.")
            print(f"El estado actual de la Rueda 1 es: {vehiculo.ruedas[0].resistencia_actual}")
            print(f"El estado actual de la Rueda 2 es: {vehiculo.ruedas[1].resistencia_actual}")
            print(f"El estado actual de la Rueda 3 es: {vehiculo.ruedas[2].resistencia_actual}")
            print(f"El estado actual de la Rueda 4 es: {vehiculo.ruedas[3].resistencia_actual}")
        elif "Moto" in str(type(vehiculo)):
            print(f"El año de la moto es {vehiculo.ano}, se encuentra actualmente desplazandose a una velocidad de {vehiculo.velocidad} km/h con un kilometraje de {vehiculo.obtener_kilometraje()} Km.")
            print(f"El estado actual de la Rueda 1 es: {vehiculo.ruedas[0].resistencia_actual}")
            print(f"El estado actual de la Rueda 2 es: {vehiculo.ruedas[1].resistencia_actual}")
        else:
            print("Vehiculo no encontrado. Intente nuevamente.")

def main():
    vehiculos = []

    # Parte 3: Completar código principal
    vehiculo = Automovil(0,2020)
    vehiculos.append(vehiculo)

    vehiculo = Moto(0,2019,10)
    vehiculos.append(vehiculo)

    # NO MODIFICAR
    vehiculo = None

    dict_opciones = {
        1: ("Seleccionar Vehiculo", seleccionar),
        2: ("Acelerar", accion),
        3: ("Frenar", accion),
        4: ("Avanzar", accion),
        5: ("Reemplazar Rueda", accion),
        6: ("Mostrar Estado", accion),
        0: ("Salir", None)
    }

    opcion = -1
    while opcion != 0:

        for llave, valor in dict_opciones.items():
            print(f"{llave}: {valor[0]}")

        try:
            opcion = int(input("Opción: "))
            print()

        except ValueError:
            print("Ingrese opción válida.")
            opcion = -1

        if opcion != 0 and opcion in dict_opciones.keys():
            if opcion == 1:
                vehiculo = dict_opciones[opcion][1](vehiculos)
            else:
                if vehiculo is None and vehiculos:
                    vehiculo = vehiculos[0]
                if vehiculo is None:
                    print("Aún no hay vehículos...")
                else:
                    dict_opciones[opcion][1](vehiculo, opcion)
        elif opcion == 0:
            pass
        else:
            print("Ingrese opción válida.")
            opcion = -1

        print()


if __name__ == "__main__":
    main()
