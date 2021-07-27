MAX_DURABILITY = 100
MIN_DURABILITY = 1
COST = 33

class Item():

    level = 1
    durability = 100
    status = True

    def __init__(self):
        self.level = 1
        self.durability = MAX_DURABILITY
        self.status = True

    def failed(self):
        self.durability -= COST

        if (self.durability == 1):
            self.status = False

    def success(self):
        self.durability = MAX_DURABILITY
        self.level = self.level + 1

    def toString(self):
        return 'Level :' + self.level + ', Durability : ' + self.durability + ', Status : ' + self.status
        
            
