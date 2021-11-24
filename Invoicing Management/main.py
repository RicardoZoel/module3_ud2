import controler
from datetime import datetime
import matplotlib.pyplot as plt


def readId():
    while True:
        Id=(input("Id:"))
        if Id.isdecimal:
            return Id
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
def readNif():
    Leter="TRWAGMYFPDXBNIZSQVHKCKE"
    while True:
        DNI=(input("Nif:"))
        DNInum=DNI[:-1]
        letter=DNI[-1]
        if len(DNI)==9 and DNI[:-1].isdigit():
            DNInum=int(DNInum)
            num = DNInum%23

            if DNI[-1].upper()!=Leter[num]:
                print("La letra del Nif no esta bien")
            else:
                return DNI
        else:
            print("El formato del Nif no esta bien")
def readPaid():
    while True:
        paid=(input("Paid(Y/N):"))
        if paid=="Y":
            return True
        elif paid=="N":
            return False
def readBase():
    while True:
        try:
            value=(float)(input("Base:"))
            return value
        except:
            print("Base must be float")
def readVat():
    while True:
        try:
            value=(float)(input("Vat:"))
            return value
        except:
            print("Vat must be float")

def readInvoice_lines():
    list_inv=[]
    while True:
        product=None
        Qantity=None
        Total=None
        while True:
            product=(input("Product:"))
            if len(product)>2 and product.isdigit:
                break
        while True:
            try:
                Qantity=(int)(input("Qantity:"))
                break
            except:
                print("Qantity must be int")
        while True:
            try:
                Total=(int)(input("Total:"))
                break
            except:
                print("Total must be int")
        tuples=(product,Qantity,Total)
        list_inv.append(tuples)       
        while True:
            exit=(input("do you want to continue?(Y/N):"))
            if exit=="Y":
                None
            elif exit=="N":
                return list_inv
            print("incorrect char")


def Add():
    Id=readId()
    Date=readDate()
    CustomerNIF=readNif()
    Paid=readPaid()
    Base=readBase()
    Vat=readVat()
    Total=Base*Vat
    Invoice_lines=readInvoice_lines()

    if contr.addInvoice(Id,Date,CustomerNIF,Paid,Base,Vat,Total,Invoice_lines):
        print("Succsecefull")
    else:
        print("Fail")
def rata():
    invoicesNotPaid=contr.getNotPaid()
    for elem in invoicesNotPaid:
        print(elem,": False")
def noRata():
    invoicesPaid=contr.getYesPaid()
    for elem in invoicesPaid:
        print(elem,": True")

def paid():
    Id=readId()
    if contr.searchIDPaid(Id):
        print("This invoice its now Paided")
    else:
        print("The invoice was already paid or does not exist")

contr=controler.controler()
while(True):
    print("1.- Add invoice")
    print("2.- List not paid invoices: All and by Customer NIF")
    print("3.- List paid invoices: All and by Customer NIF")
    print("4.- Pay invoice")
    print("5.- Exit")
    option=(int)(input("Choose option:"))
    if(option==1):
        Add()
    elif(option==2):
        rata()
    elif(option==3):
        noRata()
    elif(option==4):
        paid()
    elif(option==5):
        break