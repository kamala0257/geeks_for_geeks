from typing import List

class Solution:
    def lexicographicallyLargest(self, arr: List[int]) -> List[int]:
        n = len(arr)
        i = 0
        
        while i < n:
            j = i
            # Find the end of the current same-parity segment
            while j < n and (arr[j] % 2 == arr[i] % 2):
                j += 1
            
            # Sort the segment from i to j-1 in descending order
            arr[i:j] = sorted(arr[i:j], reverse=True)
            i = j
            
        return arr
