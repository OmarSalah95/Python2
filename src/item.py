class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def getItem(self):
        print(f'------ITEM------\n*** Name: {self.name}\n*** Item Description: {self.description}')
        