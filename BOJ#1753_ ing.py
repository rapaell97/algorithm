import sys
sys.stdin = open('a.txt', 'r')
import heapq

def dijkstra(i, k):
    queue = []
    queue.append()
V, E = map(int, input().split())
K = int(input())

graph = [[0] * (V + 1) for _ in range(V + 1)]

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u][v] = w

for i in graph:
    for k in i:
        print(k, end=' ')
    print()
