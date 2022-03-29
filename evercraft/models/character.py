# this is where your character code will go

class Character():
    character = {
        'name': ""
    }

    # def __init__(self, name):
    #     self.name = name
    
    def set_name(self, character=None):
        self.name = character['name']
        default_user = 'User'
        if key in character.keys():
            self.name = character.values()
        else:
            self.name = default_user


    def get_name(self):
        return self.name


    


         
        
