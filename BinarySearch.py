class BinarySearch:
    def __init__(self, arr: list[int]):
        self.arr = arr
    
    
    def Search(self, search: int) -> int:
        start = self.arr[0]
        end = len(self.arr - 1)
        
        middle_search = lambda start, end: ((start + end) // 2)
        
        while(True):
            middle = middle_search(start, end) 
            
            if self.arr[middle] == search:
                return middle
            elif start > end:
                return -1
            elif self.arr[middle] < search:
                start = middle
            else:
                end = middle