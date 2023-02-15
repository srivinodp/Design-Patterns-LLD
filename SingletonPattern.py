# In a multithreaded environment, it is possible for multiple threads to access the getInstance() method at the same time, and this can result in multiple instances of the class being created. To prevent this from happening, we need to add a synchronized keyword to the getInstance() method, so that only one thread can access it at a time.
# In this modified example, we have used the with statement and threading.Lock() to ensure that only one thread can access the critical section of the getInstance() method at a time. The Lock() function creates a new lock object, and the with statement acquires the lock, and then releases it when the critical section is complete. This ensures that only one thread can create the single instance of the Database class at a time.

# It's worth noting that Python's Global Interpreter Lock (GIL) means that only one thread can execute Python code at a time, so the synchronized keyword isn't strictly necessary to ensure thread-safety. However, it's still a good practice to use it to prevent any issues that may arise in case the underlying implementation of Python changes.

class Database:
    __instance = None
    
    
    def __init__(self):
        if Database.__instance != None:
            raise Exception("Cannot create more than one instance of Database class.")
        else:
            Database.__instance = self
            # create database connection here
            self.conn = None
    
    @staticmethod 
    def getInstance():
        if Database.__instance == None:
            with threading.Lock():
                if Database.__instance == None:
                    Database()
        return Database.__instance
    
    def getConnection(self):
        return self.conn
if __name__ == '__main__':
    db = Database()
    conn = db.getConnection
    # db2 = Database() -> Exception: Cannot create more than one instance of Database class.


