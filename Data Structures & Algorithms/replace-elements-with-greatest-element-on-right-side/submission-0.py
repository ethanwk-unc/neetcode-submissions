class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            x = i + 1
            max = 0
            while x < len(arr):
                if arr[x] > max:
                    max = arr[x]
                x += 1
                arr[i] = max
        arr[-1] = -1
        return arr