from collections import defaultdict, Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #counting all elements
        counter = Counter(nums)
        heap = []

        #for all elements in the counter
        for key, val in counter.items():
            #if we have less elements in heap than k
            #we add an element to k
            if len(heap) < k:
                heapq.heappush(heap, (val, key))

            #else we add element to k and 
            #just pop the lowest freq one
            else:
                heapq.heappushpop(heap, (val,key))
        
        #output is the heap[1] element
        return [h[1] for h in heap]

    