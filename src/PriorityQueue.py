import numpy as np


class PriorityQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__n_itens = 0
        self.__values = np.empty(self.__capacity, dtype=int)
    
    
    def __queue_empty(self):
        return (self.__n_itens == 0)
    
    
    def __queue_full(self):
        return (self.__n_itens == self.__capacity)
    
    
    def Queue(self, value:int):
        if self.__queue_full():
            print("Queue is full!")
            return
        
        if self.__n_itens == 0:
            self.__values[self.__n_itens] = value
            self.__n_itens += 1
        else:
            x = self.__n_itens - 1
            while x >= 0:
                if value > self.__values[x]:
                    self.__values[x + 1] = self.__values[x]
                else:
                    break
                x -= 1
            self.__values[x + 1] = value
            self.__n_itens += 1
    
    
    def Unqueue(self):
        if self.__queue_empty():
            print("Queue is empty!")
            return
        
        value = self.__values[self.__n_itens - 1]
        self.__n_itens -= 1
        return value
    
    
    def Show(self):
        if self.__queue_empty():
            return -1
        return self.__values[self.__n_itens - 1]