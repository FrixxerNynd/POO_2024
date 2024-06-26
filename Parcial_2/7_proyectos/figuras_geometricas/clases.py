class Figuras:
    def __init__(self,x,y,visible):
        self.x = x
        self.y = y
        visible = input("El objeto sera visible? (Si/No").upper
        if visible == "SI":
           self.visible = True
        elif visible == "NO":
           self.visible = False
    
    def estaVisible(self):
        return print(f"Visibilidad: {self.visble}")
    
    def setMostrar(self):
        print("El objeto se esta mostrando en las posiciones ´X´ = {self.x] y ´Y´ = {self.y}")

    def setOcultar(self):
        print("El objeto se ha ocultado")
        
    def setMover(self, x, y):
        self.x = x
        self.y = y
        print("Las posiciones fueron cambiadas correctamente")
    
class Rectangulos(Figuras):
    def __init__(self, x, y, visible, alto, ancho):
        super().__init__(x, y, visible)
        __self.alto = alto
        __self.ancho = ancho
    
    def CalcularArea(self, alto, ancho):
        alto = float(input("Ingresa la altura del rectangulo: "))
        ancho = float(input("Ingresa la anchura del rectangulo: "))
        area = alto * ancho
        return print(f"El area de la figura es: {area}")
    
class Circulos(Figuras):
    def __init__(self, x, y, visible, radio):
        super().__init__(x, y, visible)
        __self.radio = radio
    
    def calcularArea(self, radio):
        resultado = (__self.radio * 3.1416) /2