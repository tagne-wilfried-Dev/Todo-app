from app import app
from app.models.Task import Task
from app.models.TaskDAO import TaskDAO
    
class TaskService:
    
    def __init__(self):
        self.taskDAO = TaskDAO()

    def getAll(self):
        return self.taskDAO.findAll()
    
    def getEnded(self):
        return self.taskDAO.findTaskEnded()
    
    def getPending(self):
        return self.taskDAO.findTaskPending()
    
    def getNextId(self):
        return self.taskDAO.findNextId()
    
    def getTaskById(self, id):
        return self.taskDAO.findById(id)
    
    def newTask(self, task_dict):
        self.taskDAO.addTask(task_dict)
    
    def dropTask(self, id):
        if self.taskDAO.deleteTask(id):
            return self.taskDAO.updateTaskId(id)
        
    def taskAccomplished(self, id):
        return self.taskDAO.setTaskEnded(id)
    
    def taskPending(self, id):
        return self.taskDAO.taskPending(id)