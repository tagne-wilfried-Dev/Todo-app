
CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    state INTEGER DEFAULT 0,
    start DATETIME DEFAULT CURRENT_TIMESTAMP,
    end DATETIME DEFAULT NULL
)
-- ESSAYER D'UPDATE LES ID automatiquement en:
-- comptant a chaque fois le nombre de taches COUNT(*)
-- en conservant l'id de la tache a supprimer et update les ID de toutes
-- les taches suivantes en decrementant leurs ID
-- pour l'ID, ce champ est readonly et il s'agit de prendre le last ID dans la BD et y ajouter 1