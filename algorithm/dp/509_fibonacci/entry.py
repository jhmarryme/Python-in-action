from algorithm.common.test_entry import run_performance_test
from better_dp import Solution as BetterDPSolution
from dp import Solution as DPSolution
from memo_recursion import Solution as MemoSolution
from recursion import Solution as RecursionSolution

if __name__ == "__main__":
    # 解决方案类列表
    TEST_CLASSES = [
        RecursionSolution,  # 普通递归
        MemoSolution,  # 记忆化递归
        DPSolution,  # 动态规划
        BetterDPSolution,  # 优化空间版动态规划
    ]

    TEST_PARAMS = [3, 5, 20]  # 测试参数

    report = run_performance_test(
        solution_classes=TEST_CLASSES,
        method_name="fib",  # 要测试的方法名
        test_params=TEST_PARAMS,
        report_title="斐波那契算法性能与复杂度对比"
    )

    with open("fib_performance_report.md", "w", encoding="utf-8") as f:
        f.write(report)
