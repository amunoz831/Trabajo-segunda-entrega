import tkinter as tk
from estacion import Estacion


class InterfazGrafica:

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Sistema de Alquiler de Bicicletas")


        self.sistema=Estacion()

        self.usuario_label = tk.Label(ventana, text="Registro de Usuario:")
        self.usuario_label.pack()

        self.nombre_label = tk.Label(ventana, text="Nombre:")
        self.nombre_label.pack()
        self.nombre_entry = tk.Entry(ventana)
        self.nombre_entry.pack()

        self.correo_label = tk.Label(ventana, text="Correo:")
        self.correo_label.pack()
        self.correo_entry = tk.Entry(ventana)
        self.correo_entry.pack()

        self.identificacion_label = tk.Label(ventana, text="Identificación:")
        self.identificacion_label.pack()
        self.identificacion_entry = tk.Entry(ventana)
        self.identificacion_entry.pack()

        self.registrar_usuario_button = tk.Button(ventana, text="Registrar Usuario", command=self.registrar_usuario)
        self.registrar_usuario_button.pack()

        self.bicicleta_label = tk.Label(ventana, text="Número de Serie de Bicicleta:")
        self.bicicleta_label.pack()

        self.numero_serie_entry = tk.Entry(ventana)
        self.numero_serie_entry.pack()

        self.alquilar_button = tk.Button(ventana, text="Alquilar Bicicleta", command=self.alquilar_bicicleta)
        self.alquilar_button.pack()

        self.devolver_button = tk.Button(ventana, text="Devolver Bicicleta", command=self.devolver_bicicleta)
        self.devolver_button.pack()

        self.resultado_label = tk.Label(ventana, text="")
        self.resultado_label.pack()

        self.bicicletas_disponibles_label = tk.Label(ventana, text="Bicicletas Disponibles:")
        self.bicicletas_disponibles_label.pack()

        self.bicicletas_disponibles_listbox = tk.Listbox(ventana)
        self.bicicletas_disponibles_listbox.pack()

        self.tarifa_label = tk.Label(ventana, text="")
        self.tarifa_label.pack()

        self.actualizar_lista_bicicletas_disponibles()
 
