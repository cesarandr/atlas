import sqlite3

class Database():

    def __init__(self, path):
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()
        self.__setup()
        
    def __setup(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users 
                            (name TEXT PRIMARY KEY NOT NULL, 
                            password TEXT NOT NULL, 
                            tasks_done INT, 
                            created DATE);""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS sheets 
                            (name TEXT PRIMARY KEY NOT NULL,
                            status BIT NOT NULL,
                            created DATE NOT NULL,
                            finished DATE,
                            user_name TEXT NOT NULL,
                            CONSTRAINT sheet_user_FK FOREIGN KEY (user_name) REFERENCES users(name));""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS tasks 
                            (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            note TEXT,
                            status BIT NOT NULL,
                            user_name TEXT NOT NULL,
                            sheet_name TEXT NOT NULL,
                            duedate DATE NOT NULL,
                            created DATE NOT NULL,
                            finished DATE,
                            CONSTRAINT tasks_sheet_FK FOREIGN KEY (sheet_name) REFERENCES sheets(name),
                            CONSTRAINT tasks_user_FK FOREIGN KEY (user_name) REFERENCES users(name));""")


    # insert values
    def add_user(self, name, password):
        pass

    def add_task(self, name, user_name, sheet_name, duedate, note=None):
        pass

    def add_sheet(self, name):
        pass

    # delete values
    def delete_user(self, name):
        pass # think of deleting all tasks and sheets of the user

    def delete_sheet(self, name):
        pass # delete all tasks of this sheet too

    def delete_task(self, name, user, id=None):
        pass

    # update values
    def update_user(self, name=None, password=None):
        pass

    def update_task(self, name=None, user_name=None, sheet_name=None, duedate=None, note=None, status=None):
        pass

    def update_sheet(self, name=None, user_name=None, finished=None, status=None):
        pass

    # spezialized functions
    def set_task_status(self, status):
        pass

    def set_sheet_status(self, status):
        pass

    def add_task_to_sheet(self, task, sheet):
        pass

    def delete_task_from_sheet(self, task, sheet):
        pass



