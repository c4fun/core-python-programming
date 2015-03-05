__author__ = 'Richard'


class UserDatabase(object):
    'new address book entry that includes more personal info'
    def __init__(self, nm, ph, homeAddr = '', relationship = '',
                 birthday = '19700101'): #constructor
        self.name = nm
        self.phone = ph
        self.homeAddr = homeAddr
        self.relationship = relationship
        self.birthday = birthday
        print("Created instance for:", self.name)