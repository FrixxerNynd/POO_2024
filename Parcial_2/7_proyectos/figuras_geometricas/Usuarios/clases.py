
class Usuarios:
    def __init__(self, nombre, direccion, tel):
        self.nombre = nombre
        self.direccion = direccion
        self.tel = tel
    
    def setNombre(self, nombre):
        self.nombre=nombre
    
    def getNombre(self):
        return self.nombre
    
    def setDireccion(self, direccion):
        self.direccion = direccion
    
    def getDireccion(self):
       return self.direccion

    def setTel(self, tel):
        self.tel = tel

    def getTel(self):
        return self.tel

    def info_usuario(self):
        return print(f"Los datos ingresados del usuario son los siguiente: \n Nombre: {self.nombre} \n Direccion: {self.direccion} \n Telefono: {self.tel}")
    
class Clientes(Usuarios):
    def __init__(self, nombre, direccion, tel, num_cliente):
        super().__init__(nombre, direccion, tel)
        self.__num_cliente = num_cliente
    
    def setNUM_Cliente(self, num_cliente):
        self.__num_cliente = num_cliente

    def getNum_Cliente(self):
        return self.__num_cliente

    def info_Cliente(self):
        return print(f"Los datos ingresados del Cliente son los siguiente: \n Nombre: {self.nombre} \n Direccion: {self.direccion} \n Telefono: {self.tel} \n El numero del cliente registrado es: {self.__num_cliente}")

class Empleados(Usuarios):
    def __init__(self, nombre, direccion, tel, salario, num_empleado, tipo):
        super().__init__(nombre, direccion, tel)
        self._salario = salario
        self._num_empleado = num_empleado
        self._tipo = tipo
    
    def getSalario(self):
        return self._salario
    
    def setSalario(self, salario):
        self._salario = salario
    
    def setNum_Empleado(self, num_empleado):
        self._num_empleado = num_empleado
    
    def getNum_Empleado(self):
        return self._num_empleado
    
    def setTipo(self, tipo):
        self._tipo = tipo
    
    def getTipo(self):
        return self._tipo
    
    def info_Empleado(self):
        return print(f"Los datos ingresados del Empleado son los siguiente: \n Nombre: {self.nombre} \n Direccion: {self.direccion} \n Telefono: {self.tel} \n El numero del empleado registrado es: {self._num_empleado} \n El salario del empleado es de {self._salario} \n El tipo de empleado es {self._tipo}")