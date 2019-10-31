# Implement a class to hold room information. This should have name and
# description attributes.

class Room: 
    def __init__(self, name, desc, *item):
        self.name = name
        self.desc = desc
        self.items = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        