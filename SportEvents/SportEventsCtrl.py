import SportEventsModel
import random

class SportEventsCtrl():
    def __init__(self):
        self.__Events={}

    def addEvent(self,name,Date,Location,province,price):
        Event=SportEventsModel.SportEventsModel(name,Date,Location,province,price)
        if name in self.__Events.keys():
            return False
        self.__Events[name]=Event
        return True

    def getFinished(self):
        finish=[]
        for elem in self.__Events.values():
            if elem.getFinished():
                finish.append(elem)
        return finish

    def getNotFinished(self):
        finish=[]
        for elem in self.__Events.values():
            if elem.getFinished():
                None
            else:
                finish.append(elem)
        return finish
    def addParticipant(self, participant):
        model=SportEventsModel.SportEventsModel()
        model.addParticipant_to_List(participant)

    def addListOfParticipants(self, list):
        model=SportEventsModel.SportEventsModel()
        model.setList_of_participants(list)
    def finished(self,name):
        obj=self.__Events[name]
        if len(obj.getList_of_participants())>3:
            obj.finishEvent()
            first=random.choice([obj.getList_of_participants()])
            while(True):
                second=random.choice([obj.getList_of_participants()])
                if second != first:
                    break
            while(True):
                THIRD=random.choice([obj.getList_of_participants()])
                if THIRD != first:
                    if THIRD != second:
                        break
            obj.podium(first,second,THIRD)
            return True
        return False