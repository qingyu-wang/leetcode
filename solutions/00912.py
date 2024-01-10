"""
912. Sort an Array
https://leetcode.com/problems/sort-an-array/description/
"""

from typing import List


class Solution:

    # 1. Bubble Sort
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Bubble Sort
        Time:  O(n) - O(n^2)
        Space: O(1)
        """
        for i in range(len(nums)-1, 0, -1): # Parse first N-1 value
            for j in range(0, i):
                if nums[j] > nums[j+1]: # Compare with two values
                    nums[j+1], nums[j] = nums[j], nums[j+1] # Move smaller velue to the front
        return nums

    # 2. Selection Sort
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Selection Sort
        Time:  O(n^2)
        Space: O(1)
        """
        for i in range(0, len(nums)-1): # Parse first N-1 value
            t = i
            for j in range(i+1, len(nums)): # Compare with other values
                if nums[j] < nums[t]: # Find minimum value
                    t = j
            nums[i], nums[t] = nums[t], nums[i] # Move minimum value to the front
        return nums

    # 3. Insertion Sort
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Insertion Sort
        Time:  O(n^2)
        Space: O(1)
        """
        for i in range(0, len(nums)):
            for j in range(i-1, 0-1, -1):
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i -= 1
                else:
                    break
        return nums

    # 4. Quick Sort 1
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Quick Sort
        Time:  O(nlogn) - O(n^2)
        Space: O(logn)
        """
        if len(nums) > 1:
            key = nums[0]
            nums_l = []
            nums_r = []
            for i in nums[1:]:
                if i <= key:
                    nums_l.append(i)
                else:
                    nums_r.append(i)
            nums_l = self.sortArray(nums_l)
            nums_r = self.sortArray(nums_r)
            nums = nums_l + [key] + nums_r
        return nums

    # 4. Quick Sort 2
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Quick Sort
        Time:  O(nlogn)
        Space: O(logn)
        """
        def quickSort(arr, i, j):
            if i < j:
                p = partition(arr, i, j)
                quickSort(arr, i, p-1)
                quickSort(arr, p+1, j)
            return

        def partition(arr, i, j):
            r = i # Reference
            arr[r], arr[j] = arr[j], arr[r] # Move reference to the end
            p = i # Partition
            for k in range(i, j): # Compare all first N-1 elements with the reference (last one)
                if arr[k] < arr[j]:
                    arr[k], arr[p] = arr[p], arr[k] # Move smaller element to the partition
                    p += 1 # Move forward partition
            arr[j], arr[p] = arr[p], arr[j] # Move reference (last one) to the partition
            return p

        quickSort(
            arr=nums,
            i=0,
            j=len(nums)-1
        )
        return nums

    # 5. Merge Sort
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Merge Sort
        Time:  O(nlogn)
        Space: O(n)
        """
        def mergesort(arr):
            arr_len = len(arr)
            if arr_len > 1:
                arr_p = arr_len//2
                arr = merge(
                    arr_l=mergesort(arr[:arr_p]),
                    arr_r=mergesort(arr[arr_p:])
                )
            return arr

        def merge(arr_l, arr_r):
            arr_l_len = len(arr_l)
            arr_r_len = len(arr_r)
            arr_new = []
            idx_l = 0
            idx_r = 0
            while idx_l < arr_l_len and idx_r < arr_r_len:
                if arr_l[idx_l] <= arr_r[idx_r]:
                    arr_new.append(arr_l[idx_l])
                    idx_l += 1
                else:
                    arr_new.append(arr_r[idx_r])
                    idx_r += 1
            if idx_l == arr_l_len:
                arr_new += arr_r[idx_r:]
            else:
                arr_new += arr_l[idx_l:]
            return arr_new

        nums = mergesort(arr=nums)
        return nums

    # 6. Counting Sort
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Heap Sort
        Time:  O(n+k)
        Space: O(k)
        """
        arr = nums

        # Step 1. Find maximum and minimum
        arr_min = arr[0]
        arr_max = arr[0]
        for i in arr[1:]:
            if i < arr_min:
                arr_min = i
            if i > arr_max:
                arr_max = i
        arr_count = [0] * (arr_max-arr_min+1)

        # Step 2. Counting
        for i in arr:
            arr_count[i-arr_min] += 1

        # Step 3. Restore
        tick_s = 0
        for i in range(len(arr_count)):
            tick_e = tick_s + arr_count[i]
            arr[tick_s:tick_e] = [i+arr_min] * arr_count[i]
            tick_s = tick_e
        nums = arr

        return nums

    # 7. Bucket Sort
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Heap Sort
        Time:  O(n+k)
        Space: O(n+k)
        """
        bucket_num = 10
        arr_bucket = [[] for _ in range(bucket_num)]

        arr = nums
        # Step 1. Find maximum and minimum
        arr_min = arr[0]
        arr_max = arr[0]
        for i in arr[1:]:
            if i < arr_min:
                arr_min = i
            if i > arr_max:
                arr_max = i
        bucket_interval = (arr_max-arr_min)/(bucket_num-1)

        if bucket_interval != 0:

            # Step 2. Put into bucket
            for i in arr:
                arr_bucket[int((i-arr_min)/bucket_interval)].append(i)

            # Step 3. Sort each bucket
            def quick_sort(arr, i, j):
                if i < j:
                    p = partition(arr, i, j)
                    quick_sort(arr, i, p-1)
                    quick_sort(arr, p+1, j)
                return

            def partition(arr, i, j):
                r = i # Reference
                arr[r], arr[j] = arr[j], arr[r] # Move reference to the end
                p = i # Partition
                for k in range(i, j): # Compare all first N-1 elements with the reference (last one)
                    if arr[k] < arr[j]:
                        arr[k], arr[p] = arr[p], arr[k] # Move smaller element to the partition
                        p += 1 # Move forward partition
                arr[j], arr[p] = arr[p], arr[j] # Move reference (last one) to the partition
                return p

            for i in range(len(arr_bucket)):
                quick_sort(arr_bucket[i], i=0, j=len(arr_bucket[i])-1)

            print(arr_bucket)

            # Step 4. Restore
            arr_new = []
            for i in range(len(arr_bucket)):
                arr_new.extend(arr_bucket[i])
            nums = arr_new

        return nums

    # 8. Radix Sort
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Radix Sort (Integer)
        Time:  O(n*k)
        Space: O(n+k)
        """
        arr = nums

        # Step 1. Find digit number
        digit_num = 0
        for i in arr:
            digit_num_curr = len(str(abs(i)))
            if digit_num < digit_num_curr:
                digit_num = digit_num_curr

        # Step 2. Sorting
        for i in range(digit_num):
            div = 10 ** i
            mod = 10 ** (i+1)
            arr_bucket = [[] for _ in range(10)]
            for j in arr:
                arr_bucket[abs(j)%mod//div].append(j)

            if i != (digit_num-1):
                tick_s = 0
                for arr_sub in arr_bucket:
                    tick_e = tick_s + len(arr_sub)
                    arr[tick_s:tick_e] = arr_sub
                    tick_s = tick_e

        # Step 3. Sorting Last Bucket considering negative
        arr_new = []
        for arr_sub in arr_bucket:
            for i in arr_sub:
                if i < 0:
                    arr_new = [i] + arr_new
                else:
                    arr_new = arr_new + [i]

        nums = arr_new
        return  nums

    # 9. Heap Sort
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Heap Sort
        Time:  O(nlogn)
        Space: O(1)
        """
        def heapify(arr, idx, cur_len):
            idx_l = 2*idx+1
            idx_r = 2*idx+2
            idx_max = idx
            # Find maximum position (right has higher priority)
            if idx_l < cur_len and arr[idx_l] > arr[idx_max]:
                idx_max = idx_l
            if idx_r < cur_len and arr[idx_r] > arr[idx_max]:
                idx_max = idx_r
            # Swap position between maximum and reference
            if idx_max != idx:
                arr[idx], arr[idx_max] = arr[idx_max], arr[idx]
                # heapify the reference at new position
                heapify(arr=arr, idx=idx_max, cur_len=cur_len)
            return

        arr = nums
        arr_len = len(arr)

        # Build maxheap (move larger one from leaf to root and from right to left)
        for idx in range(arr_len//2, -1, -1): # From N/2 (last parent) to 0 (1st)
            heapify(arr=arr, idx=idx, cur_len=arr_len)

        for cur_len in range(arr_len-1, 0, -1): # From N-1 (last) to 1 (2nd)
            # Swap position between reference (leaf) and maximum (root)
            arr[cur_len], arr[0] = arr[0], arr[cur_len]
            # Move reference from root to leaf
            # Move maximum from leaf to root
            heapify(arr=arr, idx=0, cur_len=cur_len)
        return nums
