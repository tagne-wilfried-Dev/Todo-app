
class TaskDAOInterface:
    
    def findAll(self):
        """ premet de trouver toutes les taches et
            renvoit une liste d'objets Task"""
        pass
    
    def findById(self,id):
        """ premet de trouver une tache par son id
            renvoit un objet Task"""
        pass
    
    def addTask(self,task):
        """ Ajoute une nouvelle tache dans la bd"""
        pass
    
    def deleteTask(self, id):
        """ supprime une tache par son id """
        pass
    
    def updateTaskId(self, deletedTaskId):
        """ update tous les id des taches suivant la tache supprimee
            en les decrementant"""
        pass
    
    def setTaskEnded(self,id):
        """ met a jour l'etat d'une tache a accomplie """
        pass
    