class NQueue:
    # Initialize your data structure.
    def __init__(self, n, s):
        self.arr = [None] * s
        self.front = [None] * n
        self.rear = [None] * n
        self.after = [i+1 for i in range(s-1)] + [None]
        self.freeSpot = 0
        self.size = n

    # Enqueues 'X' into the Mth queue. Returns true if it gets pushed into the queue, and false otherwise.
    def enqueue(self, x, m):
        if self.freeSpot is None:
            return False

        # Get first free spot
        idx = self.freeSpot

        # Update free spot
        self.freeSpot = self.after[idx]
        
        if self.front[m-1] is None:
            # If no front
            self.front[m-1] = idx
        else:
            # Link new elem to prev elem
            self.after[self.rear[m-1]] = idx
        
        # Update after
        self.after[idx] = None

        # Update rear
        self.rear[m-1] = idx

        # Push element
        self.arr[idx] = x

        return True

    # Dequeues top element from Mth queue. Returns -1 if the queue is empty, otherwise returns the popped element.
    def dequeue(self, m):
        if self.front[m-1] is None:
            return -1
        
        # Find index to pop
        idx = self.front[m-1]

        # Update front
        self.front[m-1] = self.after[idx]

        # Update free slots
        self.after[idx] = self.freeSpot
        self.freeSpot = idx

        return self.arr[idx]