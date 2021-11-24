class Model:
    def __init__(self,dni,name,surname,age,city,province,email):
        self.__DNI=dni
        self.__Name=name
        self.__Surnames=surname
        self.__Age =age
        self.__City =city
        self.__Province=province
        self.__Email=email
        
    def getDNI(self):
        return self.__DNI

    def setName(self,nom):
        self.__Name=nom
    def getName(self):
        return self.__Name

    def setSurnames(self,Sut):
        self.__Surnames=Sut
    def getSurnames(self):
        return self.__Surnames

    def setAge(self,Age):
        self.__Age=Age
    def getAge(self):
        return self.__Age
    
    def setCity(self,City):
        self.__City=City
    def getCity(self):
        return self.__City

    def setProvince(self,Province):
        self.__Province=Province
    def getProvince(self):
        return self.__Province

    def setEmail(self,Email):
        self.__Email=Email
    def getEmail(self):
        return self.__Email

