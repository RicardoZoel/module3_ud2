import Model


class controler():

    def __init__(self):
        self.__Students={}
        
    def addStudent(self,Dni,Name,Surname,Age,City,Province,Email):
        studient=Model.Model(Dni,Name,Surname,Age,City,Province,Email)
        if Dni in self.__Students.keys():
            return False
        self.__Students[Dni]=studient
        return True

    def pop(self,dni):
        if dni in self.__Students.keys():
            studient=self.__Students.pop(dni)
            return studient
        else:
            return None
    def searchStudent(self, student):
        return self.__Students.get(student)

    def modify(self, dni, properties):
        student = self.__Students.get(dni)