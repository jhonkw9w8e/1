class Usuario:
    def __init__(self, idUsuario, nombre, contraseña):
        self.idUsuario = idUsuario
        self.nombre = nombre
        self.contraseña = contraseña

    def getNombre(self):
        return self.nombre

class Administrador:
    def __init__(self, idAdmin):
        self.idAdmin = idAdmin

class Chef:
    def __init__(self, nombre, experiencia):
        self.nombre = nombre
        self.experiencia = experiencia

    def getExperiencia(self):
        return self.experiencia

class Ingrediente:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

class Receta:
    def __init__(self, nombre, idReceta, preparacion, personas):
        self.nombre = nombre
        self.idReceta = idReceta
        self.preparacion = preparacion
        self.personas = personas
        self.ingredientes = []

    def agregarIngrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

    def listarIngredientes(self):
        return [ingrediente.nombre for ingrediente in self.ingredientes]

    def editarIngrediente(self, nombre_viejo, nombre_nuevo):
        for ingrediente in self.ingredientes:
            if ingrediente.nombre == nombre_viejo:
                ingrediente.nombre = nombre_nuevo
                break

    def consultarIngredientes(self):
        return [(ingrediente.nombre, ingrediente.cantidad) for ingrediente in self.ingredientes]


# Crear instancias de las clases
usuario1 = Usuario(1, 'Juan', 'contraseña123')
administrador1 = Administrador(101)
chef1 = Chef('Carlos', 5)

# Crear ingredientes y recetas
ingrediente1 = Ingrediente('Harina', 500)
ingrediente2 = Ingrediente('Azúcar', 300)
receta1 = Receta('Torta de Chocolate', 1, 'Mezclar y hornear', 8)

# Agregar ingredientes a la receta
receta1.agregarIngrediente(ingrediente1)
receta1.agregarIngrediente(ingrediente2)

# Consultar ingredientes de la receta
print("Ingredientes de la receta:", receta1.listarIngredientes())

# Editar un ingrediente de la receta
receta1.editarIngrediente('Azúcar', 'Azúcar glass')
print("Ingredientes editados de la receta:", receta1.listarIngredientes())
    



        
    
