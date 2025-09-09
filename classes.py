class Locadora:
    def __init__(self):
        self.name = "Locadora EndOfWorld"
        self.town = "Itupeva"
        self.costumers = []
        self.items = []

# -----------------------------------------------------------

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

# -----------------------------------------------------------

class Film(Item):
    def __init__(self, code, title, genre, duration):
        super().__init__(code, title)
        self.__genre = genre
        self.__duration = duration

    def getName(self):
        return self.__title
    
    def getGenre(self):
        return self.__genre

    def getDuration(self):
        return self.__duration

    def setName(self, title):
            self.__title = title

    def setGenre(self, genre):
            self.__genre = genre 
        
    def setDuration(self, duration):
            self.__duration = duration
            
class Game(Item):
    def __init__(self, code, title, platform, age_range):
        super().__init__(code, title)
        self.__platform = platform
        self.__age_range = age_range

    def getName(self):
        return self.__title
    
    def getPlatform(self):
        return self.__platform

    def getAgeRange(self):
        return self.__age_range

    def setName(self, title):
            self.__title = title

    def set(self, platform):
            self.__platform = platform 
        
    def setDuration(self, age_range):
            self.__age_range = age_range

# -----------------------------------------------------------

class Costumer():
    def __init__(self, name, cpf):
        self.__name = name
        self.__cpf = cpf
        self.__rented_items = []

    def alocateItem(self, item: Item):
        self.__rented_items.append(item)

    def returnItem(self, item: Item):
        self.__rented_items.pop(item)
