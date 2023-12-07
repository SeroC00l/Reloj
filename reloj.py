from time import strftime
import tkinter as tk
from PIL import Image, ImageDraw, ImageFont, ImageTk

# Ruta de tu fuente TTF personalizada
ruta_fuente_personalizada = './font/DS-DIGIB.TTF'

# Configuración de estilo de la ventana emergente
estilo_ventana = {
    'title': 'Reloj Digital',
    'text_font': (ruta_fuente_personalizada, 160, 'bold'),  # Utiliza la fuente personalizada
    'text_color': 'white',
    'background_color': 'black',
    'outline_color': '#333',
    'outline_thickness': 4,  # Grosor del contorno
}

class RelojDigital(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.overrideredirect(True)
        self.wm_attributes('-transparentcolor', 'black')

        self.label = tk.Label(
            self,
            font=estilo_ventana['text_font'],
            fg=estilo_ventana['text_color'],
            bg=estilo_ventana['background_color'],
            bd=0,
        )
        self.label.pack(expand=True, fill='both')

        self.actualizar_hora()

    def agregar_contorno(self, texto):
        imagen = Image.new('RGBA', (1000, 200), (0, 0, 0, 0))
        dibujo = ImageDraw.Draw(imagen)
        fuente = ImageFont.truetype(estilo_ventana['text_font'][0], estilo_ventana['text_font'][1])

        # Configurar el contorno
        contorno_config = {
            "fill": estilo_ventana['outline_color'],  # Cambiado a 'outline_color'
            "width": estilo_ventana['outline_thickness'],  # Cambiado a 'outline_thickness'
        }

        # Dibujar el texto con contorno
        dibujo.text((0, 0), texto, font=fuente, stroke_width=estilo_ventana['outline_thickness'], stroke_fill=estilo_ventana['outline_color'])

        # Dibujar el texto principal
        dibujo.text((0, 0), texto, font=fuente, fill=estilo_ventana['text_color'])

        self.label.img = ImageTk.PhotoImage(imagen)
        self.label['image'] = self.label.img

    def actualizar_hora(self):
        hora_texto = strftime('%H:%M:%S %p')
        self.agregar_contorno(hora_texto)
        self.after(1000, self.actualizar_hora)

def centrar_ventana(ventana):
    ventana.update_idletasks()
    ancho_ventana = ventana.winfo_width()
    alto_ventana = ventana.winfo_height()
    x_pantalla = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2 + 150
    y_pantalla = ventana.winfo_screenheight() // 2 - alto_ventana // 2 - 150
    ventana.geometry('+{}+{}'.format(x_pantalla, y_pantalla))

if __name__ == "__main__":
    root = tk.Tk()  # Crear una instancia de Tk para ocultar la ventana principal de fondo
    root.withdraw()  # Ocultar la ventana principal de fondo
    reloj = RelojDigital()
    reloj.attributes('-topmost', False)  # Establecer a False para colocar detrás de todas las ventanas
    centrar_ventana(reloj)
    reloj.mainloop()