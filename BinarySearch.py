class BinarySearch:
    def __init__(self, arr: list[int]):
        self.arr = arr
    
    
    def Search(self, search: int) -> int:
        start = self.arr[0]
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
        arr_lenght = len(self.arr)
        
        for i in range(arr_lenght - 1):
            if (self.arr[i + 1] > number):
                self.arr[i+1: arr_lenght-1] = range(self.arr[i], arr_lenght)
                self.arr[i] = number
                break
        self.arr[arr_lenght] = number
        