# inf
inf = float('inf')

# copy list
a = [1, 2, 3]
b = a[:]

# reverse
b = a[::-1]

# array of size n
a = [0] * n

# 2d array
a = [[0] * w for _ in range(h)]
a = [[0 for x in range(w)] for y in range(h)]

# loop
for a in range(n): pass              # 0, 1, ... , n - 1
for a in range(n - 1, -1, -1): pass  # n - 1, n - 2, ... , 0

# stack
dfs = []
dfs.append(child)  # push
curr = dfs.pop()

# queue
import collections
bfs = collections.deque()
bfs.append(child)     # push
curr = bfs.popleft()  # pop

# priority queue
import heapq
pq = []
heapq.heappush(pq, child)  # push
next = heapq.heappop(pq)   # pop
