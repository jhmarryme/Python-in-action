'''
是不是树
描述

树是一个很重要的数据结构，它是由很多节点组成，节点与节点之间相连（树的边），我们定义树如下：

(1) 树有且只有一个根节点，根节点是指没有任何节点连接到的节点。
(2) 树没有回路连接
(3) 树的根节点之外的节点，都必须有且只有一个节点指向该节点。

一个聪明的程序员不走寻常路，他给树中的每个节点一个整数编号（整个树中编号唯一，且编号都是正整数），用一个节点编号对表示树中的边（第一个编号表示起始节点，第二个编号表示结束节点），这样他就可以用一组编号对表示整个树了。


用一组编号对表示这个树就是，(6,4),(6,1),(6,9),(4,5),(1,7),(1,2),(9,8)。用这种表示方法，与给出的编号对出现的顺序无关，如上图中的树，也可以表示成(4,5),(1,7),(1,2),(9,8),(6,4),(6,1),(6,9)。

为了统一，当且仅当树只有一个节点时，只用一个编号对表示此树，如下图可以表示为(8,8)。

现在这个聪明的程序员用树的这种表示方法维护了他的系统中的所有相关的树结构的数据。后来，由于一部分数据损坏，需要判断哪些树结构的数据损坏了（即给出的这组树的编号对没有办法表示一个树）。请你写一段代码帮助他判断哪些树的数据被损坏。


输入
一个数组a表示一组编号对，数组的长度为偶数。如上图中，a=[6,4,6,1,6,9,4,5,1,7,1,2,9,8]

输出
true或者false表示给出的这个组编号对是否可以组成树。


输入样例 1
a=[6,4,6,1,6,9,4,5,1,7,1,2,9,8]

输出样例 1
true

函数定义风格如下:
def solve(a: list, size: int) -> bool:
    return False

'''

# 答案正确
def solve(a: list, size: int) -> bool:
    from collections import defaultdict

    if size == 0:
        return False

    if size % 2 != 0:
        return False

    pairs = [(a[i], a[i + 1]) for i in range(0, size, 2)]

    if len(pairs) == 1:
        p, c = pairs[0]
        if p == c:
            return True
        else:
            return True

    else:
        for p, c in pairs:
            if p == c:
                return False

        unique_nodes = set()
        in_degree = defaultdict(int)

        for p, c in pairs:
            unique_nodes.add(p)
            unique_nodes.add(c)
            in_degree[c] += 1

        num_edges = len(pairs)

        expected_nodes = num_edges + 1

        if len(unique_nodes) != expected_nodes:
            return False

        roots = [node for node in unique_nodes if in_degree[node] == 0]

        if len(roots) != 1:
            return False

        root = roots[0]

        for node in unique_nodes:
            if node == root:
                continue
            if in_degree[node] != 1:
                return False

        node_list = list(unique_nodes)
        node_index = {node: i for i, node in enumerate(node_list)}
        parent_array = [i for i in range(len(node_list))]

        def find(u):
            while parent_array[u] != u:
                parent_array[u] = parent_array[parent_array[u]]
                u = parent_array[u]
            return u

        def union(u, v):
            pu = find(u)
            pv = find(v)
            if pu == pv:
                return False
            parent_array[pu] = pv
            return True

        for p, c in pairs:
            u = node_index[p]
            v = node_index[c]
            if not union(u, v):
                return False

        root_rep = find(0)
        for i in range(1, len(node_list)):
            if find(i) != root_rep:
                return False

        return True


# =============================
# Sample Test Cases
# =============================
if __name__ == "__main__":
    # Test Case 1: Example Input 1 (Valid Tree)
    a1 = [6, 4, 6, 1, 6, 9, 4, 5, 1, 7, 1, 2, 9, 8]
    size1 = len(a1)
    print(solve(a1, size1))  # Expected Output: True

    # Test Case 2: Single-Node Tree (Valid)
    a2 = [8, 8]
    size2 = len(a2)
    print(solve(a2, size2))  # Expected Output: True

    # Test Case 3: Two-Node Tree (Valid)
    a3 = [1, 2]
    size3 = len(a3)
    print(solve(a3, size3))  # Expected Output: True

    # Test Case 4: Single Pair with Distinct Nodes (Valid)
    a4 = [1, 2]
    size4 = len(a4)
    print(solve(a4, size4))  # Expected Output: True

    # Test Case 5: Invalid Tree with Cycle
    a5 = [1, 2, 2, 3, 3, 1]
    size5 = len(a5)
    print(solve(a5, size5))  # Expected Output: False

    # Test Case 6: Invalid Tree with Multiple Roots
    a6 = [1, 2, 3, 4]
    size6 = len(a6)
    print(solve(a6, size6))  # Expected Output: False

    # Test Case 7: Valid Larger Tree
    a7 = [1, 2, 1, 3, 1, 4, 2, 5, 2, 6, 3, 7, 3, 8]
    size7 = len(a7)
    print(solve(a7, size7))  # Expected Output: True

    # Test Case 8: Invalid Tree with Multiple Parents
    a8 = [1, 2, 3, 2]
    size8 = len(a8)
    print(solve(a8, size8))  # Expected Output: False

    # Test Case 9: Valid Tree with More Nodes
    a9 = [10, 20, 10, 30, 20, 40, 30, 50]
    size9 = len(a9)
    print(solve(a9, size9))  # Expected Output: True

    # Test Case 10: Invalid Tree Due to Disconnected Components
    a10 = [1, 2, 3, 4, 5, 6]
    size10 = len(a10)
    print(solve(a10, size10))  # Expected Output: False
