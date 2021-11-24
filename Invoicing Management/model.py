class model():
    def __init__(self,Id,Date,CustomerNIF,Paid,Base,Vat,Total,Invoice_lines):
        self.__Id=Id
        self.__Date=Date
        self.__CustomerNIF=CustomerNIF
        self.__Paid =Paid
        self.__Base =Base
        self.__Vat=Vat
        self.__Total=Total
        self.__Invoice_lines=Invoice_lines
    
        
    def getId(self):
        return self.__Id

    def setDate(self,Date):
        self.__Date=Date
    def getDate(self):
        return self.__Date

    def setCustomerNIF(self,CustomerNIF):
        self.__CustomerNIF=CustomerNIF
    def getCustomerNIF(self):
        return self.__CustomerNIF

    def setPaid(self,Paid):
        self.__Paid=Paid
    def getPaid(self):
        return self.__Paid
    
    def setBase(self,Base):
        self.__Base=Base
    def getBase(self):
        return self.__Base

    def setVat(self,Vat):
        self.__Vat=Vat
    def getVat(self):
        return self.__Vat

    def setTotal(self,Total):
        self.__Total=Total
    def getTotal(self):
        return self.__Total

    def setInvoice_lines(self,Invoice_lines):
        self.__Invoice_lines=Invoice_lines
    def getInvoice_lines(self):
        return self.__Invoice_lines