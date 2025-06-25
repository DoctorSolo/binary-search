# @DoctorSolo
#
#   This class adds some values into a circular queue, because
#   circular queue is more efficient than standard queue.

import numpy as np


class CircularQueue:
    def __init__(self, capacity:int):
        self.__capacity:int   = capacity
        self.__start:int      = 0
        self.__end:int        =-1
        self.__n_itens:int    = 0
        self.__values = np.empty(self.__capacity, dtype=int)
    
    
    def __queue_empty(self) -> bool:
        return (self.__n_itens == 0)
    
    
    def __queue_full(self) -> bool:
        return (self.__n_itens == self.__capacity)
    
    
    def Queue(self, value:int):
        if self.__queue_full():
            print("Queue is full!")
            return
        
        if self.__end == (self.__capacity - 1):
            self.__end = -1
        self.__end += 1
        self.__values[self.__end] = value
        self.__n_itens += 1
    
    
    def Unqueue(self):
        if self.__queue_empty():
            print("Queue is empty!")
            return
        temp = self.__values[self.__start]
        self.__start += 1
        if self.__start == (self.__capacity - 1):
            self.__start = 0
        self.__n_itens -= 1
        return temp
    
    
    def Show(self):
        if self.__queue_empty():
            return - 1
        return self.__values[self.__start]