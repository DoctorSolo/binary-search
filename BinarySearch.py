class BinarySearch:
    def __init__(self, arr: list[int]):
        self.arr = arr
    
    
    def Search(self, search: int) -> int:
        start = self.arr[0]
        end = len(self.arr) - 1
        
        middle_search = lambda start, end: ((start + end) // 2)
        
        while(start <= end):
            middle = middle_search(start, end) 
            
            if self.arr[middle] == search:
                return middle
            elif self.arr[middle] < search:
                start = middle + 1
            else:
                end = middle - 1
        return -1
    
    