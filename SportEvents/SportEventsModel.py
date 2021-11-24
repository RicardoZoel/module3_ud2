class SportEventsModel:
    def __init__(self,name,Date,Location,province,price):
        self.__Name=name
        self.__Date=Date
        self.__Location =Location
        self.__Province=province
        self.__price =price
        self.__T_event=0
        self.__List_of_participants=[]
        self.__Finished=False
        self.__Podium={}

    def setList_of_participants(self,List_of_participants):
        self.__List_of_participants=List_of_participants
    def getList_of_participants(self):
        return self.__List_of_participants
    def addParticipant_to_List(self,participant):
        self.__List_of_participants.append(participant)
        self.__T_event+=1

    def finishEvent(self):
        self.__Finished=True
    def getFinished(self):
        return self.__Finished

    def getName(self):
        return self.__Name

    def podium(self,FIRST, SECOND ,THIRD):
        self.__Podium["FIRST"]=FIRST
        self.__Podium["SECOND"]=SECOND
        self.__Podium["THIRD"]=THIRD

    