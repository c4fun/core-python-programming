class NewAddrBookEntry:
    'new address book entry class'
    def __init__(self, nm, ph): #constructor
        self.name = Name(nm)      #create Name instance
        self.phone = Phone(ph)    #create Phone instance
        print("Created instance for:", self.name)

class Name():
    'new name class'
    def __init__(self, nm):
        self.name = nm

class Phone():
    'new Phone class'
    def __init__(self, ph):
        self.phone = []
        for x in ph:
            self.phone.append(x)

class PersonalAddrBookEntry(NewAddrBookEntry):
    'new address book entry that includes more personal info'
    def __init__(self, nm, ph, homeAddr = '', relationship = '',
                 birthday = '19700101'): #constructor
        #Use the super to inherit the parent's __init__ function
        super(PersonalAddrBookEntry, self).__init__()
        self.homeAddr = homeAddr
        self.relationship = relationship
        self.birthday = birthday
        print("Created instance for:", self.name)
        
    
    def updateHomeAddr(self, homeAddr):
        self.homeAddr = homeAddr
        print("The home address is updated to: ", self.homeAddr)
    def update_relationship(self, relationship):
        self.relationship = relationship
        print("The relationship is updated to: ", self.relationship)

