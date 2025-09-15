from algorithm.common.test_entry import run_performance_test
from double_for import Solution as DoubleForSolution
from dp import Solution as DPSolution

if __name__ == "__main__":
    # https://leetcode.cn/problems/triangle/solutions/329394/di-gui-ji-yi-hua-dp-bi-xu-miao-dong-by-sweetiee/
    # 解决方案类列表
    TEST_CLASSES = [
        DoubleForSolution,  # 普通双层for 循环
        DPSolution,  # 动态规划
    ]

    TEST_PARAMS = [[-1], [-2, 1, -3, 4, -1, 2, 1, -5, 4], [1], [5, 4, -1, 7, 8]]  # 测试参数

    report = run_performance_test(
        solution_classes=TEST_CLASSES,
        method_name="maxSubArray",  # 要测试的方法名
        test_params=TEST_PARAMS,
        report_title="最大子数组和算法性能对比"
    )

    with open("max_subarray_performance_report.md", "w", encoding="utf-8") as f:
        f.write(report)
