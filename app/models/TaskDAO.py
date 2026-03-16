
import sqlite3
from app import app
from app.models.TaskDAOInterface import TaskDAOInterface
from app.models.Task import Task
class TaskDAO(TaskDAOInterface):
    
    def __init__(self):
        self.dbName = app.root_path + '/database/database.db'
        self._initTable()
        
    def _getDbConnection(self):
        conn = sqlite3.connect(self.dbName)
        conn.row_factory = sqlite3.Row
        return conn
            
    def _initTable(self):
        query = """
            CREATE TABLE IF NOT EXISTS tasks(
                id INTEGER NOT NULL PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT,
                state INTEGER DEFAULT 0,
                start DATETIME DEFAULT CURRENT_TIMESTAMP,
                end DATETIME DEFAULT NULL
            )"""
        conn = self._getDbConnection()
        conn.execute(query)
        conn.commit()
        conn.close()
                
                
    def findAll(self):
        """ premet de trouver toutes les taches et
            renvoit une liste d'objets Task"""
        conn = self._getDbConnection()
        query = "SELECT * FROM tasks"
        tasks = conn.execute(query)
        taskList = list()
        for task in tasks:
            taskList.append(Task(dict(task)))
        conn.close()
        return taskList
    
    def findTaskEnded(self):
        """ premet de trouver toutes les taches terminees et
            renvoit une liste d'objets Task"""
        conn = self._getDbConnection()
        query = "SELECT * FROM tasks WHERE state=1 "
        tasks = conn.execute(query)
        taskList = list()
        for task in tasks:
            taskList.append(Task(dict(task)))
        conn.close()
        if  taskList:
            return taskList
        else:
            return []
    
    def findTaskPending(self):
        """ premet de trouver toutes les taches en cours et
            renvoit une liste d'objets Task"""
        conn = self._getDbConnection()
        query = "SELECT * FROM tasks WHERE state=0"
        tasks = conn.execute(query)
        taskList = list()
        for task in tasks:
            taskList.append(Task(dict(task)))
        conn.close()
        if  taskList:
            return taskList
        else:
            return []
        
    def findNextId(self):
        """ renvoit l'ID de la prochaine tache a ajouter """   
        conn = self._getDbConnection()
        query = " SELECT MAX(id) FROM tasks "
        result = conn.execute(query).fetchone()
        for maxId in result:
            if isinstance(maxId,int):
                return maxId
        return 0
        
         
    
    def findById(self,id):
        """ premet de trouver une tache par son id
            renvoit un objet Task"""
        conn = self._getDbConnection()
        query = "SELECT * FROM tasks WHERE id=:id"
        tasks = conn.execute(query, {"id":id})
        if tasks:
            task = Task(dict(tasks))
            return task
        else:
            return None
        
        
    
    def addTask(self, task):
        """ Ajoute une nouvelle tache dans la bd """
        conn = self._getDbConnection()
        added = False
        query = """
                INSERT INTO tasks(id,name,description) VALUES(:id,:name,:description)
                """
        if conn.execute(query,{"id":task['id'],"name":task['name'],"description":task['description']}):
            added = True
            conn.commit()
        conn.close()
        return added
            
    def deleteTask(self, id):
        """ supprime une tache par son id """
        conn = self._getDbConnection()
        deleted = False
        query = """
                DELETE FROM tasks WHERE id=:id
                """
        if conn.execute(query,{"id":id}):
            deleted = True
            conn.commit()
        conn.close()
        return deleted
    
    def deleteEndedTasks(self):
        """Supprime toutes les taches terminees """
        conn = self._getDbConnection()
        query = "DELETE FROM tasks WHERE state=1 "
        conn.execute(query)
        conn.commit()
        conn.close()
        return True
        
    def updateTaskId(self, deletedTaskId):
        """ update tous les id des taches suivant la tache supprimee
            en les decrementant"""
        conn = self._getDbConnection()
        query = "UPDATE tasks SET id=id-1 WHERE id>:id"
        if conn.execute(query,{"id":deletedTaskId}):
            conn.commit()
            return True
        else:
            return False          
        
    def setTaskEnded(self,id):
        """ met a jour l'etat d'une tache a accomplie """
        conn = self._getDbConnection()
        query = "UPDATE tasks SET state=1 WHERE id=:id"
        setEndDateQuery = "UPDATE tasks SET end=CURRENT_TIMESTAMP WHERE id=:id"
        if conn.execute(query,{"id":id}):
            if conn.execute(setEndDateQuery,{"id":id}):
                conn.commit()
                return True
        else:
            return False
        
    def taskPending(self, id):
        """ met a jour l'etat d'une tache a encours """
        conn = self._getDbConnection()
        query = "UPDATE tasks SET state=0 WHERE id=:id"
        resetEndDateQuery = "UPDATE tasks SET end=NULL WHERE id=:id"
        if conn.execute(query,{"id":id}):
            if conn.execute(resetEndDateQuery,{"id":id}):
                conn.commit()
                return True
        else:
            return False
        
        