class Locadora:
    def __init__(self):
        self.name = "Locadora EndOfWorld"
        self.town = "Itupeva"
        self.costumers = []
        self.items = []

class Item:
    def __init__(self, code, title):
        self.__code = code
        self.__title = title
        self.__status = True #Check if it's available

    def rent(self): #Rent a tape if it's available
        if self.__status:
            self.__status = False
    
    def returnTape(self): #Return a tape if it's not avaiable 
        if not self.__status:
            self.__status = True

class Film(Item):
    def __init__(self, code, genre, duration):
        self.__code = code
        self.__genre = genre
        self.__duration = duration


        
