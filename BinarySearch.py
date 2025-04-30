class BinarySearch:
    def __init__(self, arr: list[int]):
        self.arr = list(arr)
    
    
    def Search(self, search: int) -> int:
        start = 0
        end = len(self.arr) - 1
        
        while(start <= end):
            middle = ((start + end) // 2)
            
            if self.arr[middle] == search:
                return middle
            elif self.arr[middle] < search:
                start = middle + 1
            else:
                end = middle - 1
        return -1
    
    
    def Add(self, number:int) -> None:
        
        self.arr.append(-1)
        arr_lenght = len(self.arr) - 1
        
        if arr_lenght == 1:
            self.arr[arr_lenght] = number
            return
        
        if self.arr[arr_lenght-1] < number:
            self.arr[arr_lenght] = number
            return
        
        for i in range(arr_lenght):
            if (self.arr[i] > number):
                self.arr[i+1: arr_lenght+1] = self.arr[i: arr_lenght]
                self.arr[i] = number
                return
        return SystemError("something went wrong")
    
    
    def Delete(self, number:int) -> None:
        arr_lenght = len(self.arr) - 1
        
        if (self.arr[0] > number > self.arr(arr_lenght)):
            return SystemError("This number not in list")
        
        position = self.Search(number)
        
        if position == -1:
            return SystemError("This number not in list")
        
        self.arr[position:arr_lenght] = self.arr[position+1:arr_lenght+1]
        self.arr.pop()
    
    
    def Show(self) -> None:
        for i in range(len(self.arr)):
            print(f"{i} --------> {self.arr[i]}")
        