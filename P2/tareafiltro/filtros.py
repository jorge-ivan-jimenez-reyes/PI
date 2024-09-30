import sys
import cv2
import numpy as np
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QScrollArea, QVBoxLayout, QPushButton, QFileDialog, QWidget
)

class InterfazFiltros(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Aplicador de Filtros')
        self.setGeometry(100, 100, 800, 600)
        
        # Layout principal
        self.contenedor = QWidget()
        self.layout_principal = QVBoxLayout(self.contenedor)
        
        # Área de scroll para mostrar imágenes y filtros
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_contenido = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_contenido)
        self.scroll_area.setWidget(self.scroll_contenido)
        self.layout_principal.addWidget(self.scroll_area)
        
        # Botón para cargar imagen
        self.btn_cargar = QPushButton('Cargar Imagen')
        self.btn_cargar.clicked.connect(self.cargar_imagen)
        self.layout_principal.addWidget(self.btn_cargar)
        
        self.setCentralWidget(self.contenedor)

    def cargar_imagen(self):
        archivo, _ = QFileDialog.getOpenFileName(
            self, 'Seleccionar Imagen', '', 'Imagen (*.png *.jpg *.bmp)')
        if archivo:
            self.imagen_original = cv2.imread(archivo)
            self.imagen_gris = cv2.cvtColor(self.imagen_original, cv2.COLOR_BGR2GRAY)  # Convertir a escala de grises
            self.mostrar_filtros()

    def aplicar_filtro_promedio(self, imagen):
        return cv2.blur(imagen, (5, 5))

    def aplicar_filtro_mediano(self, imagen):
        return cv2.medianBlur(imagen, 5)

    def aplicar_filtro_laplaciano(self, imagen):
        laplaciano = cv2.Laplacian(imagen, cv2.CV_64F)
        return cv2.convertScaleAbs(laplaciano)

    def aplicar_filtro_gradiente(self, imagen):
        grad_x = cv2.Sobel(imagen, cv2.CV_64F, 1, 0, ksize=5)
        grad_y = cv2.Sobel(imagen, cv2.CV_64F, 0, 1, ksize=5)
        grad_x = cv2.convertScaleAbs(grad_x)
        grad_y = cv2.convertScaleAbs(grad_y)
        return cv2.addWeighted(grad_x, 0.5, grad_y, 0.5, 0)

    def mostrar_imagen(self, imagen, titulo):
        if len(imagen.shape) == 2:  # Si es imagen en escala de grises
            q_image = QImage(imagen.data, imagen.shape[1], imagen.shape[0], 
                             imagen.shape[1], QImage.Format.Format_Grayscale8)
        else:  # Si es imagen en color (aunque no lo usamos aquí)
            imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
            h, w, ch = imagen_rgb.shape
            bytes_per_line = ch * w
            q_image = QImage(imagen_rgb.data, w, h, bytes_per_line,
                             QImage.Format.Format_RGB888)
        
        pixmap = QPixmap.fromImage(q_image)
        label_imagen = QLabel()
        label_imagen.setPixmap(pixmap.scaled(
            400, 400, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        label_titulo = QLabel(titulo)
        self.scroll_layout.addWidget(label_titulo)
        self.scroll_layout.addWidget(label_imagen)
        
        btn_descargar = QPushButton(f'Descargar {titulo}')
        btn_descargar.clicked.connect(
            lambda: self.descargar_imagen(imagen, titulo))
        self.scroll_layout.addWidget(btn_descargar)

    def mostrar_filtros(self):
        self.scroll_layout.addWidget(QLabel('Imagen Original en Escala de Grises'))
        self.mostrar_imagen(self.imagen_gris, 'Original en Escala de Grises')
        
        # Filtros de suavizado
        imagen_promedio = self.aplicar_filtro_promedio(self.imagen_gris)
        self.mostrar_imagen(imagen_promedio, 'Filtro Promedio (Grises)')
        
        imagen_mediana = self.aplicar_filtro_mediano(self.imagen_gris)
        self.mostrar_imagen(imagen_mediana, 'Filtro Mediano (Grises)')
        
        # Filtros de detección de bordes
        imagen_laplaciana = self.aplicar_filtro_laplaciano(self.imagen_gris)
        self.mostrar_imagen(imagen_laplaciana, 'Filtro Laplaciano (Grises)')
        
        imagen_gradiente = self.aplicar_filtro_gradiente(self.imagen_gris)
        self.mostrar_imagen(imagen_gradiente, 'Filtro Gradiente (Grises)')

    def descargar_imagen(self, imagen, titulo):
        archivo, _ = QFileDialog.getSaveFileName(
            self, 'Guardar Imagen', f'{titulo}.png', 'Imagen (*.png *.jpg *.bmp)')
        if archivo:
            cv2.imwrite(archivo, imagen)

app = QApplication(sys.argv)
ventana = InterfazFiltros()
ventana.show()
sys.exit(app.exec())
