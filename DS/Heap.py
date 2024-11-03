

# Heapq is by default a minimum heap
# Build Min Heap (Heapify)
# Time: O(n), Space: O(1)
A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
import heapq
heapq.heapify(A)
print("Original heap: ", A)


# Heap Push (Insert element)
# Time: O(log n)
heapq.heappush(A, 4)
print("Added a 4: ", A)


# Heap Pop (Extract min)
# Time: O(log n)
minn = heapq.heappop(A)
print("Popped from the top: ", A, minn)


# Heap Sort
# Time: O(n log n), Space: O(n)
def heapsort(arr):
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0] * n
    for i in range(n): 
        minn = heapq.heappop(arr)
        new_list[i] = minn
    return new_list

print("Heapsort: ", heapsort([1, 3, 5, 2, -32, 7, 6, 999]))

# Heap Push Pop
# Time: O(log n)
heapq.heappushpop(A, 99)
print("Pushed 99 and popped the minimum: ", A)

# Peak at min:
# Time: O(1)
print("Peak: ", A[0])


print("\n\n")
# TO make a max heap
# We need to negate all the numbers 

B = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
n = len(B)

for i in range(n):
    B[i] = -B[i]

heapq.heapify(B)
print("Max heap: ", B)

# Output the largest: 
largest = -heapq.heappop(B)
print("Largest: ", largest)

# Adding to max heap
heapq.heappush(B, -7)
print("Inserted 7 into the max heap: ", B)


print("\n\n")


# Build heap from scratch:
# Time: O(n log n)
# Slower than heapify 
C = [-5, 4, 2, 4, 4, 9, 60, 2, -31]

heap = []

print("Building heap from scratch: ")
for x in C:
    heapq.heappush(heap, x)
    print(heap)

print("\n\n")

# IMPORTANT FOR LEETCODE
# Putting tuples of items on the heap
D = [5, 4, 3, 5, 4, 3, 5, 5, 4]

from collections import Counter
counter = Counter(D)
print("Counter: ", counter)

heap = []
# Loop through the counter: 
for k, v in counter.items(): 
    heapq.heappush(heap, (v, k))

print("Putting tupple into the heap: ", heap)
