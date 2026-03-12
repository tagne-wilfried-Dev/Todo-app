
class Task:
    
    def __init__(self,dict):
        self.id = dict['id']
        self.name = dict['name']
        self.description = dict['description']
        self.state = dict['state']
        self.start = dict['start']
        self.end = dict['end']