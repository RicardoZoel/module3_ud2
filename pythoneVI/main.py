import Model
import controler
import re

def readDNI():
    Leter="TRWAGMYFPDXBNIZSQVHKCKE"
    while True:
        DNI=(input("Dni:"))
        DNInum=DNI[:-1]
        letter=DNI[-1]
        if len(DNI)==9 and DNI[:-1].isdigit():
            DNInum=int(DNInum)
            num = DNInum%23

            if DNI[-1].upper()!=Leter[num]:
                print("La letra del DNI no esta bien")
            else:
                return DNI
        else:
            print("El formato del DNI no esta bien")

def readName():
    while True:
        Name=(input("Name:"))
        if len(Name)>0:
            return Name
        else:
            print("Nombre incorrecto")


def readSurname():
    while True:
        Surname=(input("Surname:"))
        if len(Surname)>0:
            return Surname
        else:
            print("Surname incorrecto")

def readCity():
    while True:
        City=(input("City:"))
        if len(City)>0:
            return City
        else:
            print("City incorrecto")
    
def readAge():
    while True:
        Age=(input("Age:"))
        if Age.isdigit:
            return Age
        else:
            print("Age incorrecto")

def readProvince():
    while True:
        Province=(input("Province:"))
        if len(Province)>0:
            return Province
        else:
            print("Province incorrecto")

def readEmail():
    while True:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' 
        Email=(input("Email:"))
    
        if(re.fullmatch(regex, Email)):
            return Email
 
        else:
            print("Invalid Email")
    
    
def Modifi(dni):
    student = contr.searchStudent(dni)
    if student != None:
        print("Modification of student with DNI: ", dni)
        print("1.- Modify Name")
        print("2.- Modify Surname")
        print("3.- Modify Age")
        print("4.- Modify City")
        print("5.- Modify Province")
        print("6.- Modify Email")
        optionM=(int)(input("What do you want to modify:"))
        if(optionM==1):
            Name=readName()
        elif(optionM==2):
            Surname=readSurname()
        elif(optionM==3):
            Age=readAge()
        elif(optionM==4):
            City=readCity()
        elif(optionM==5):
            Province=readProvince()
        elif(optionM==6):
            Email=readEmail()
    
def Add():
    Dni=readDNI()
    Name=readName()
    Surname=readSurname()
    Age=readAge()
    City=readCity()
    Province=readProvince()
    Email=readEmail()
    if contr.addStudent(Dni,Name,Surname,Age,City,Province,Email):
        print("Succsecefull")
    else:
        print("Fail")

contr=controler.controler()
while(True):
    print("STUDENT CRUD")
    print("----------------------------")
    print("1.- Add a student")
    print("2.- Delete a student")
    print("3.- Modify a student")
    print("4.- Search a student")
    print("5.- Exit")
    option=(int)(input("Choose option:"))
    if(option==1):
        Add()
    elif(option==2):
        dni=readDNI()
        student= contr.pop(dni)
        if student!=None:
            print("Succsecefull")
        else:
            print("Dni not exist")
    elif(option==3):
        dni=readDNI()
        Modifi()
    elif(option==4):
        pass
    elif(option==5):
        break