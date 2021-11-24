import SportEventsCtrl
from datetime import datetime
import re

def readName():
    while True:
        Name=(input("Name:"))
        if len(Name)>0:
            return Name
        else:
            print("Nombre incorrecto")
def readDate():
    while True:
        Date=(input("Date(DD/MM/AAAA):"))
        try:
            dateparse=Date.split("/")
            day=int(dateparse[0])
            month=int(dateparse[1])
            year=int(dateparse[2])
            return datetime(year,month,day)
        except:
            print("Error! Date must be DD/MM/AAAA")
def readLocation():
    while True:
        Name=(input("Location:"))
        if len(Name)>0:
            return Name
        else:
            print("Location incorrecto")
def readProvince():
    while True:
        Name=(input("Province:"))
        if len(Name)>0:
            return Name
        else:
            print("Province incorrecto")
def readPrice():
    while True:
        Age=(input("Registration Price:"))
        if Age.isdigit:
            return Age
        else:
            print("Price incorrecto")

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
def readAge():
    while True:
        Age=(input("Age:"))
        if Age.isdigit:
            return Age
        else:
            print("Age incorrecto")
def readEmail():
    while True:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' 
        Email=(input("Email:"))
    
        if(re.fullmatch(regex, Email)):
            return Email
 
        else:
            print("Invalid Email")
def addParticipants():
    list_inv=[]
    while True:
        DNI=readDNI()
        NAME=readName()
        AGE=readAge()
        Email=readEmail()
        tuples=(DNI,NAME,AGE,Email)
        contr.addListOfParticipants(tuples)       
        while True:
            exit=(input("do you want to continue?(Y/N):"))
            if exit=="Y":
                None
            elif exit=="N":
                return None
            print("incorrect char")
def AddEvent():
    Name=readName()
    Date=readDate()
    Location=readLocation()
    province=readProvince()
    price=readPrice()
    if contr.addEvent(Name,Date,Location,province,price):
        print("Succsecefull")
        addParticipants()
    else:
        print("Fail")
def ListEvenPending():
    for elem in contr.getNotFinished():
        print(elem.getName(),": ",elem.getFinished())

def ListEventsFinish():
    for elem in contr.getFinished():
        print(elem.getName(),": ",elem.getFinished())

def Finish():
    count=0
    for elem in contr.getNotFinished():
        count+=1
        print(count,": ",elem.getName())
    option=input("Choose the name event is finished:")
    if contr.finished():
        print("the event is finished")
    else:
        print("the event don't have participants or not exist")


contr=SportEventsCtrl.SportEventsCtrl()
while(True):
    print("1.- Add Event")
    print("2.- Add participant to an event*")
    print("3.- List pending events with participants")
    print("4.- List events finished with podium")
    print("5.- Finish an event")
    print("5.- Exit")
    option=(int)(input("Choose option:"))
    if(option==1):
        AddEvent()
    elif(option==2):
        addParticipants()
    elif(option==3):
        ListEvenPending()
    elif(option==4):
        ListEventsFinish()
    elif(option==5):
        Finish()
    elif(option==6):
        break





