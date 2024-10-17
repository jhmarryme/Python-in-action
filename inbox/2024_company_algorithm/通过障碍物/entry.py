"""
通过障碍物
描述

在一张平面上有一些障碍物N（N<=600），这些障碍物平行于 X 轴或 Y 轴。它们可能会相交，但永远不会重叠。每个障碍物都有一个切割成本 Ci（Ci<=100）。

在障碍物的任何位置切割都是有效的，但是不能与另一个障碍物的交点处切割，请计算允许人们在平面上自由通行所需的最小成本。

输入
二维数组，每行有5个数字，前4个数字为障碍物两个端点的坐标，第五个数字为该障碍物的切割成本

输出
输出允许人们在平面上自由通行所需的最小成本

输入样例
-10 10 10 10 1
-10 -10 10 -10 2
-5 -15 -5 15 3
0 -15 0 15 4
5 -15 5 15 5
输出样例
2

这是一个函数定义格式:
def cut(a):
return 0
"""

def cut(a):
    import sys
    import math
    from collections import deque

    INF = float('inf')

    class Edge:
        def __init__(self, to, rev, cap):
            self.to = to
            self.rev = rev
            self.cap = cap

    class MaxFlow:
        def __init__(self, N):
            self.size = N
            self.graph = [[] for _ in range(N)]

        def add_edge(self, fr, to, cap):
            forward = Edge(to, len(self.graph[to]), cap)
            backward = Edge(fr, len(self.graph[fr]), 0)
            self.graph[fr].append(forward)
            self.graph[to].append(backward)

        def bfs_level(self, s, t, level):
            q = deque()
            level[:] = [-1] * self.size
            level[s] = 0
            q.append(s)
            while q:
                v = q.popleft()
                for e in self.graph[v]:
                    if e.cap > 0 and level[e.to] == -1:
                        level[e.to] = level[v] + 1
                        q.append(e.to)
                        if e.to == t:
                            return
            return

        def dfs_flow(self, v, t, upTo, iter, level):
            if v == t:
                return upTo
            for i in range(iter[v], len(self.graph[v])):
                e = self.graph[v][i]
                if e.cap > 0 and level[v] < level[e.to]:
                    d = self.dfs_flow(e.to, t, min(upTo, e.cap), iter, level)
                    if d > 0:
                        self.graph[v][i].cap -= d
                        self.graph[e.to][e.rev].cap += d
                        return d
                iter[v] += 1
            return 0

        def max_flow(self, s, t):
            flow = 0
            level = [-1] * self.size
            while True:
                self.bfs_level(s, t, level)
                if level[t] == -1:
                    break
                iter = [0] * self.size
                while True:
                    f = self.dfs_flow(s, t, INF, iter, level)
                    if f == 0:
                        break
                    flow += f
            return flow

    # 分离水平和垂直障碍物
    horizontal = []
    vertical = []
    for obstacle in a:
        x1, y1, x2, y2, c = obstacle
        if y1 == y2:
            # 水平
            x_start = min(x1, x2)
            x_end = max(x1, x2)
            horizontal.append((x_start, y1, x_end, y2, c))
        elif x1 == x2:
            # 垂直
            y_start = min(y1, y2)
            y_end = max(y1, y2)
            vertical.append((x1, y_start, x2, y_end, c))
        else:
            # 非法障碍，忽略
            pass

    U_cnt = len(horizontal)
    V_cnt = len(vertical)
    N = U_cnt + V_cnt + 2
    source = U_cnt + V_cnt
    sink = U_cnt + V_cnt + 1
    mf = MaxFlow(N)

    # 从源点连接到所有水平障碍物节点
    for i in range(U_cnt):
        c = horizontal[i][4]
        mf.add_edge(source, i, c)

    # 从所有垂直障碍物节点连接到汇点
    for i in range(V_cnt):
        c = vertical[i][4]
        mf.add_edge(U_cnt + i, sink, c)

    # 如果水平和垂直障碍物相交，则连接它们
    for i in range(U_cnt):
        h_x_start, h_y, h_x_end, _, _ = horizontal[i]
        for j in range(V_cnt):
            v_x, v_y_start, _, v_y_end, _ = vertical[j]
            if h_x_start <= v_x <= h_x_end and v_y_start <= h_y <= v_y_end:
                # 相交
                mf.add_edge(i, U_cnt + j, INF)

    # 计算最大流（等于最小割）
    result = mf.max_flow(source, sink)
    print(result)

a = [
    [-10, 10, 10, 10, 1],
    [-10, -10, 10, -10, 2],
    [-5, -15, -5, 15, 3],
    [0, -15, 0, 15, 4],
    [5, -15, 5, 15, 5]
]

cut(a)
