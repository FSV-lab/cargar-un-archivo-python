import pickle

class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

# Crear un objeto de la clase Vehiculo
mi_vehiculo = Vehiculo("Toyota", "Corolla", 2021)

# Guardar el objeto en un archivo utilizando la librería pickle
with open("mi_vehiculo.pkl", "wb") as archivo:
    pickle.dump(mi_vehiculo, archivo)

# Cargar el objeto desde el archivo
with open("mi_vehiculo.pkl", "rb") as archivo:
    mi_vehiculo_cargado = pickle.load(archivo)

# Mostrar los atributos del objeto cargado
print("Marca: ", mi_vehiculo_cargado.marca)
print("Modelo: ", mi_vehiculo_cargado.modelo)
print("Año: ", mi_vehiculo_cargado.año)
