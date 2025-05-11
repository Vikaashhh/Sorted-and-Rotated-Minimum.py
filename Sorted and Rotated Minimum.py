class Solution:
    def findMin(self, arr):
        # Binary search ka use karenge minimum element dhoondhne ke liye
        low = 0
        high = len(arr) - 1

        while low < high:
            mid = (low + high) // 2  # Array ka beech wala index

            # Agar mid element high wale se bada hai, to minimum right side me hoga
            if arr[mid] > arr[high]:
                low = mid + 1  # Right half me jao
            else:
                # Agar mid chhota ya barabar hai, to minimum left half me ya mid pe ho sakta hai
                high = mid

        # Jab loop khatam hoga, low hi minimum element ka index hoga
        return arr[low]
