class NStack:
    def __init__(self, n, s):
        # Stores elements
        self.arr = [None] * s

        # Stores next available free spot
        self.next = [i+1 for i in range(s-1)] + [-1]

        # Stores top of each stack
        self.top = [-1] * (n)

        # Stores next free spot
        self.freeSpot = 0

    # Pushes 'X' into the Mth stack. Returns true if it gets pushed into the stack, and false otherwise.
    def push(self, x, m):
        # If no empty spots, return false
        if self.freeSpot == -1:
            return False
        
        # Get the empty spot
        idx = self.freeSpot

        # Update free spot
        self.freeSpot = self.next[idx]

        # Insert element into array
        self.arr[idx] = x

        # Update next
        self.next[idx] = self.top[m-1]

        # Update top
        self.top[m-1] = idx

        return True

    # Pops top element from Mth Stack. Returns -1 if the stack is empty, otherwise returns the popped element.
    def pop(self, m):
        # If stack has no elements, return -1
        if self.top[m-1] == -1:
            return -1

        # Get top index
        idx = self.top[m-1]

        # Set new top
        self.top[m-1] = self.next[idx]

        # Update next
        self.next[idx] = self.freeSpot

        # Update freespot
        self.freeSpot = idx

        # Return element
        return self.arr[idx]
