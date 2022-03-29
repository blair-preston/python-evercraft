# this is where your character code will go

class Character():
    character = {
        'name': ""
    }

    # def __init__(self, name):
    #     self.name = name
    
    def set_name(self, character=None):
        if character == None:
            self.name = 'User'
        else:
            self.name = character["name"]

    def get_name(self):
        return self.name


    


         
        
