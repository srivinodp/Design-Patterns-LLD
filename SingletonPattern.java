// In this implementation, we have used the synchronized keyword with the getInstance() method to ensure that only one thread can access it at a time. The volatile keyword is used to make sure that the changes to the instance variable are visible to all threads.

// The synchronized keyword ensures that only one thread can execute the critical section of the getInstance() method at a time, which ensures that only one instance of the Database class is created, even in a multithreaded environment.

// Note that while the synchronized keyword can ensure thread-safety in a multithreaded environment, it can also lead to performance issues, especially if the critical section of the code is long or if there are many threads. In such cases, other synchronization techniques such as using a double-checked locking pattern or using the java.util.concurrent package may be more appropriate.
class Database {
    private static volatile Database instance;
    // private Connection conn;
    
    private Database() {
        // create database connection here
    }
    
    public static synchronized Database getInstance() {
        if (instance == null) {
            instance = new Database();
        }
        return instance;
    }
    
    // public Connection getConnection() {
    //     return conn;
    // }
}
class SingletonPattern{
    public static void main(String[] args) {
        Database db = Database.getInstance();
        // db.getConnection();
    }
}

