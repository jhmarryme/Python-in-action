from algorithm.common.test_entry import run_performance_test
from memo_recursion import Solution as MemoRecursionSolution
from recursion import Solution as RecursionSolution
from dp import Solution as DpSolution
from better_dp import Solution as BetterDpSolution

if __name__ == "__main__":
    # 解决方案类列表
    TEST_CLASSES = [
        # 递归公式: f(i,j)=min(f(i+1,j),f(i+1,j+1))+triangle[i][j]
        RecursionSolution,  # 递归
        MemoRecursionSolution,  # 记忆化递归
        DpSolution,  # 动态规划
        BetterDpSolution,  # 优化动态规划
    ]

    TEST_PARAMS = [[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], ]  # 测试参数

    report = run_performance_test(
        solution_classes=TEST_CLASSES,
        method_name="minimumTotal",  # 要测试的方法名
        test_params=TEST_PARAMS,
        report_title="三角形最小路径和算法性能对比"
    )
