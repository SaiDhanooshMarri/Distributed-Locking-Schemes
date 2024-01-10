# Distributed-Locking-Schemes
Distributed system that focused on decentralized and distributed locking techniques
Distributed Locking
• For distributed locking, a centralized server with a timestamp-based technique was used.
• Uses a queue to process requested and released access, assuring sequential access.
• The application kept track of how many attempts it took to access the file, copying distributed locking in a shared environment. 

Key Learnings
• Socket Programming: Learned how to use sockets to build communication between processes.
• Concurrency and Parallelism: Concurrent execution was achieved by mastering the use of threads and multiprocessing.
• Distributed Algorithms: Understanding and implementation of Lamport's technique for entirely ordered multicasting and the vector clock algorithm for causally ordered events have been improved.
• Locking Schemes: Decentralized and distributed locking methods were effectively devised and compared, with synchronization and coordination taken into account.

Issues Encountered
• Synchronization Challenges: Handled the complexity of synchronizing threads and processes in order to support concurrent access without conflicts.
• Debugging in Distributed Systems: Due to the asynchronous nature of processes, I faced difficulties debugging bugs in a distributed system.
