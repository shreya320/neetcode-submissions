class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        greatest = max(arr[n-1],-1)
        for i in range(n - 2, -1, -1):
            temp = arr[i]
            arr[i] = greatest
            greatest = max(temp, greatest)
        
        arr[n - 1] = -1
        return arr


