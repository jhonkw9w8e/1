# Este es un programa que almacenara información sobre empresas, sus empleados y sus clientes. Ambos se caracterizan por su nombre y edad.

class Cliente:
    # Aqui iran los atributos y funciones de la clase Cliente
    def __init__(self, DNI, Nombre, Direccion, CodigoUnico):
        self.DNI  = int(DNI)
        self.Nombre = str(Nombre)
        self.Direccion = int(Direccion)
        self.CodigoUnico = int(CodigoUnico) 
    def realizar_reserva(self):
        reserva=self.DNI - self.Nombre - self.Direccion - self.CodigoUnico
        return reserva
    def ser_avaladoporCliente(self):
        avaladoporCliente= self.Nombre

class Reserva:
    # Aqui se inicializaran los atributos y funciones de la clase Coche
    def __init__(self, FechaInicio, FechaFinal, PrecioTotal, Entregado):
        self.FechaInicio  = int(FechaInicio)
        self.FechaFinal = str(FechaFinal)
        self.PrecioTotal = int(PrecioTotal)
        self.Entregado = bool(Entregado)
    def agregarCoche(Self):
        agregarCoche= Self.FechaInicio - Self.FechaFinal - Self.PrecioTotal - Self.Entregado
class Agencia:
    # Aqui se inicializaran los atributos y funciones de la clase Agencia
    def __init__(self, Nombre):
        self.Nombre = str(Nombre)
        
class Garaje:
# Aqui se inicializaran los atributos y funciones de la clase Garaje
    def __init__(self,Nombre):
        self.Nombre = str(Nombre)
    def Cambiar_garaje(self):
        cambiar_garaje=self.nombre()


