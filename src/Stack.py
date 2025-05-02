import numpy as np

class Stack:
    def __init__(self, size:int):
        self.__size:int = size
        self.__top:int = -1
        self.__values = np.empty(self.__size, dtype=int)
    
    
    def __isEmpity(self) -> bool:
        if self.__top == -1:
            return True
        else:
            return False
    
    
    def __isFull(self) -> bool:
        if self.__top == self.__size -1:
            return True
        else:
            return False
    
    
    def Push(self, value:int) -> None:
        if self.__isFull():
            print("This stack has no more space")
        else:
            self.__top += 1
            self.__values[self.__top] = value
    
    
    def Pop(self) -> None:
        if self.__isEmpity():
            print("Stack is enpity, you can't push here")
        else:
            self.__top -= 1
    
    
    def Top(self):
        return f"{self.__top} -----> {self.__values[self.__top]}"