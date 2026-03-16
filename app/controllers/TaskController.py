
from flask import render_template, request, url_for,redirect,flash
from app import app
from app.services.TaskService import TaskService
class TaskController:
    
    taskServ = TaskService()
    @app.route("/", methods=["GET", "POST"])
    def home():
        taskList = TaskController.taskServ.getAll()
        nextId = TaskController.taskServ.getNextId() # dernier ID/ nombre de taches totales
        # les metadata contienent le nbre de taches terminees et encours
        ended = len(TaskController.taskServ.getEnded()) # nombre de tache terminees
        pending = len(TaskController.taskServ.getPending()) # nombre de tache en cours
        try:
            pct = int((ended/nextId)*100) # represente la fraction de tache terminee
        except:
            pct = 0
        return render_template('index.html', taskList = taskList, metadata = {'ended':ended,'pending':pending,"nextId":nextId,'pct':pct})
        
    @app.route('/add', methods=['POST'])    
    def newTaskAdd():
        id = request.form['id']
        name = request.form['title']
        description = request.form['description']
        if TaskController.taskServ.newTask({'id':id, 'name':name, 'description':description}):
            return redirect(url_for('home'))
        return redirect(url_for('home'))
    
    @app.route('/deleteid=<int:id>', methods=['GET'])    
    def deleteTask(id):
        TaskController.taskServ.dropTask(id)
        return redirect(url_for('home'))
    
    @app.route('/endedid=<int:id>', methods=['GET'])
    def taskEnded(id):
        TaskController.taskServ.taskAccomplished(id)
        return redirect(url_for('home'))
    
    @app.route('/pendingid=<int:id>', methods=['GET'])
    def taskPending(id):
        TaskController.taskServ.taskPending(id)
        return redirect(url_for('home'))
    @app.route('/deleteEndedTasks', methods=['GET'])
    def deleteEndedTasks():
        TaskController.taskServ.deleteEnded()
        return redirect(url_for('home'))    
            
            
        