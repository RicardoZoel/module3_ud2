import model


class controler():

    def __init__(self):
        self.__invoice={}

    def addInvoice(self,Id,Date,CustomerNIF,Paid,Base,Vat,Total,Invoice_lines):
        Invoice=model.model(Id,Date,CustomerNIF,Paid,Base,Vat,Total,Invoice_lines)
        if Id in self.__invoice.keys():
            return False
        self.__invoice[Id]=Invoice
        return True

    def getNotPaid(self):
        invoiceNotPaid=[]
        for elem in self.__invoice.values():
            if elem.getPaid() == False:
                invoiceNotPaid.append(elem.getCustomerNIF())
        return invoiceNotPaid
    
    def getYesPaid(self):
        invoicePaid=[]
        for elem in self.__invoice.values():
            if elem.getPaid() == True:
                invoicePaid.append(elem.getCustomerNIF())
        return invoicePaid

    def searchIDPaid(self,Id):
        for elem in self.__invoice.values():
            if elem.getId()==Id and elem.getPaid() == False:
                Invoice=model.model(Id,elem.getDate(),elem.getCustomerNIF(),True,elem.getBase(),elem.getVat(),elem.getTotal(),elem.getInvoice_lines())
                self.__invoice[Id]=Invoice
                return True
        return False