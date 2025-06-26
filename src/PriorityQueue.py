import numpy as np
# @DoctorSolo
#
#   This code reorders the queue
#   for priority numbers


class PriorityQueue:
    def __init__(self, capacity:int):
        self.__capacity:int = capacity  # this variable determines the capacity of the array
        self.__n_itens:int = 0          # this variable counts the numbers of elements
        self.__values = np.empty(self.__capacity, dtype=int)    # This array is our queue
    
    
    # Verify if queue is empty...
    def __queue_empty(self) -> bool:
        return (self.__n_itens == 0)
    
    
    # Verify if queue is full...
    def __queue_full(self) -> bool:
        return (self.__n_itens == self.__capacity)
    
    
    # This method is our priority queue
    def Queue(self, value:int) -> None:
        
        # Verify if queue is full, if it's full, can't add new elements.
        if self.__queue_full():
            print("Queue is full!")
            return None
        
        # To save time, if itens numers to 0, add this {value} here, and count new element.
        if self.__n_itens == 0:
            self.__values[self.__n_itens] = value
            self.__n_itens += 1
        
        # If the code falls here, {x} receive itens numbers, 
        # reorden the array and add the value in a priority place
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
    
    
    # This method unqueue this array,
    def Unqueue(self) -> (None | int):
        
        # first verify this if empty, if not, 
        if self.__queue_empty():
            print("Queue is empty!")
            return None
        
        
        # {value} receite the fisrt element in queue, 
        # in that case, the fist element is end element on array
        
        self.__n_itens -= 1
        return self.__values[self.__n_itens]
    
    
    # Only show the fisrt value...
    def Show(self) -> int:
        if self.__queue_empty():
            return -1
        return self.__values[self.__n_itens - 1]