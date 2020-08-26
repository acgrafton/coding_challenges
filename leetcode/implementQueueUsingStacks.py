"""
Implement the following operations of a queue using stacks.

    push(x) -- Push element x to the back of queue.
    pop() -- Removes the element from in front of queue.
    peek() -- Get the front element.
    empty() -- Return whether the queue is empty.

Example:

    >>> queue = MyQueue()

    >>> queue.push(1)

    >>> queue.push(2)

    >>> queue.peek()
    1
    >>> queue.pop()
    1
    >>> queue.empty()
    False

Notes:

    You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
    Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
    You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).


"""



from collections import deque

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.elements = deque()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        
        self.elements.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        
        temp = deque()
        while self.elements:
            temp.append(self.elements.pop())
        
        front_el = temp.pop()
        
        while temp:
            self.elements.append(temp.pop())
            
        return front_el
        

    def peek(self) -> int:
        """
        Get the front element.
        """

        temp = deque()
        while self.elements:
            temp.append(self.elements.pop())
        
        front_el = temp[-1]
        
        while temp:
            self.elements.append(temp.pop())
        return front_el

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        
        return not self.elements


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n** ALL TESTS PASSED. SUCCESS!! **\n')